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
'''
DOUBLE = ct.c_double
PDOUBLE = ct.POINTER(DOUBLE)
INT = ct.c_int

#matrix = ct.cdll.LoadLibrary('matrix2.dll')
#print_matrix = getattr(matrix,'print')

ptr = (DOUBLE*640*480)()
for i in range(480):
    for j in range(640):
        ptr[i][j] = 0

libc.Hexagonization(ptr,480,640)
'''

#===========================================
# Test #3
#===========================================

'''
img = np.random.random((480,640))


ptr = img.ctypes.data_as(ct.POINTER(ct.c_double))
print libc.Hexagonization(ptr,480,640)


#plt.imshow(img)
plt.figimage(img,cmap=plt.gray())
plt.show()
'''

#===========================================
# Test #4
#===========================================


#cap = cv2.VideoCapture('.\GoPro_vga.avi')
cap = cv2.VideoCapture(0)

time.sleep(1)
img = np.ones((480,640))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    dst = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    img[0:480,0:640] = dst[0:480,0:640]

    
    
    ptr = img.ctypes.data_as(ct.POINTER(ct.c_double))
    libc.Hexagonization(ptr,480,640,7)
    
    
    dst[0:480,0:640] = img[0:480,0:640] 
    
    # Display the resulting frame
    cv2.imshow('Video Processing', dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('screen.png', dst)
    #if cv2.waitKey(1) & 0xFF == ord('h'):
    #    print dst.shape

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


#===========================================
# Test END
#===========================================
del libc
