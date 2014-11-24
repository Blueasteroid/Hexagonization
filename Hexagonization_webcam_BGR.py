import ctypes as ct
import numpy as np
import cv2
import time
#import matplotlib.pyplot as plt


libc = ct.cdll.LoadLibrary(r".\Hexagonization_DLL\Hexagonization.dll")
#===========================================
# Test #1
#===========================================


# libc.Credit()


#===========================================
# Test #2
#===========================================


#cap = cv2.VideoCapture('.\GoPro_vga.avi')
cap = cv2.VideoCapture(0)

time.sleep(1)

npArray_R = np.ones((480,640))
npArray_G = np.ones((480,640))
npArray_B = np.ones((480,640))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    matArray = frame #cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    npArray_R[0:480,0:640] = matArray[0:480,0:640,0] 
    ptr_R = npArray_R.ctypes.data_as(ct.POINTER(ct.c_double))
    libc.Hexagonization(ptr_R,480,640,7)

    npArray_G[0:480,0:640] = matArray[0:480,0:640,1]
    ptr_G = npArray_G.ctypes.data_as(ct.POINTER(ct.c_double))
    libc.Hexagonization(ptr_G,480,640,7)

    npArray_B[0:480,0:640] = matArray[0:480,0:640,2]
    ptr_B = npArray_B.ctypes.data_as(ct.POINTER(ct.c_double))
    libc.Hexagonization(ptr_B,480,640,7)
    
    matArray[0:480,0:640,0] = npArray_R[0:480,0:640]
    matArray[0:480,0:640,1] = npArray_G[0:480,0:640]
    matArray[0:480,0:640,2] = npArray_B[0:480,0:640]

    timestamp = time.strftime("%d-%b-%Y_%H-%M-%S ", time.gmtime())
    cv2.putText(matArray,timestamp+'@KrappLab',(5,460),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2,cv2.CV_AA)

    # Display the resulting frame
    cv2.imshow('Video Processing', matArray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(10) & 0xFF == ord('s'):
        cv2.imwrite('.\KrappLab '+timestamp+'.png', matArray)
    #if cv2.waitKey(1) & 0xFF == ord('h'):
    #    print dst.shape

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


#===========================================
# Test END
#===========================================
del libc
