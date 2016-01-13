import ctypes as ct
import numpy as np
import cv2
import time
import sys
#import matplotlib.pyplot as plt

HEXAGON_SIZE = 15
COLOR_MODE = 0
WATER_MARKER = 1

if len(sys.argv)>1:
    HEXAGON_SIZE = int(sys.argv[1])
if len(sys.argv)>2:
    COLOR_MODE = int(sys.argv[2])
if len(sys.argv)>3:
    WATER_MARKER = int(sys.argv[3])

libc = ct.cdll.LoadLibrary(r".\Hexagonization_DLL\Hexagonization.dll")
#===========================================
# Demo
#===========================================

# libc.Credit()
print "==================="
print "Hexagonization Demo"
print "JH@Krapp Lab"
print "12/01/2016"
print "==================="
print "Parameter1: HEXAGON_SIZE. e.g. 7 or 15 or 30"
print "Parameter1: COLOR_MODE. e.g. 1 for color, 0 for gray"
print "Parameter1: WATER_MARKER. e.g. 1 for with, 0 for without"
print "Example: C:\>python hexagonization_demo.py 7 1 0 <enter>"
print "==================="
print "Press ESC key to exit the program..."
print "Press 's' key for screen shot..."
print " "

cap = cv2.VideoCapture(0)
time.sleep(1)

npArray_R = np.ones((480,640))
npArray_G = np.ones((480,640))
npArray_B = np.ones((480,640))
npArray_K = np.ones((480,640))


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    matArray = frame 

    if (COLOR_MODE == 0) :
        frame_K = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        npArray_K[0:480,0:640] = frame_K[0:480,0:640] 
        #npArray_K = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ptr_K = npArray_K.ctypes.data_as(ct.POINTER(ct.c_double))
        libc.Hexagonization(ptr_K,480,640, HEXAGON_SIZE)
        matArray[0:480,0:640,0] = npArray_K[0:480,0:640]
        matArray[0:480,0:640,1] = npArray_K[0:480,0:640]
        matArray[0:480,0:640,2] = npArray_K[0:480,0:640]
    
    elif (COLOR_MODE == 1) :
        npArray_R[0:480,0:640] = matArray[0:480,0:640,0] 
        ptr_R = npArray_R.ctypes.data_as(ct.POINTER(ct.c_double))
    #    libc.Hexagonization(ptr_R,480,640,7)
        libc.Hexagonization(ptr_R,480,640, HEXAGON_SIZE)

        npArray_G[0:480,0:640] = matArray[0:480,0:640,1]
        ptr_G = npArray_G.ctypes.data_as(ct.POINTER(ct.c_double))
    #    libc.Hexagonization(ptr_G,480,640,7)
        libc.Hexagonization(ptr_G,480,640, HEXAGON_SIZE)

        npArray_B[0:480,0:640] = matArray[0:480,0:640,2]
        ptr_B = npArray_B.ctypes.data_as(ct.POINTER(ct.c_double))
    #    libc.Hexagonization(ptr_B,480,640,7)
        libc.Hexagonization(ptr_B,480,640, HEXAGON_SIZE)
   
        matArray[0:480,0:640,0] = npArray_R[0:480,0:640]
        matArray[0:480,0:640,1] = npArray_G[0:480,0:640]
        matArray[0:480,0:640,2] = npArray_B[0:480,0:640]

    timestamp = time.strftime("%d-%b-%Y_%H-%M-%S ", time.gmtime())
    if (WATER_MARKER == 1) :
        cv2.putText(matArray,timestamp+'@KrappLab',(5,460),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2,cv2.CV_AA)

    # Display the resulting frame
    cv2.imshow('Video Processing', matArray)

    key = cv2.waitKey(10)
    if key & 0xFF == 27: #...ESC key to exit
        break
    if key & 0xFF == ord('s'): #...'s' key for save image
        cv2.imwrite('.\KrappLab '+timestamp+'.png', matArray)
    #if cv2.waitKey(1) & 0xFF == ord('h'):
    #    print dst.shape

#===========================================
# Test END
#===========================================
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

del libc
