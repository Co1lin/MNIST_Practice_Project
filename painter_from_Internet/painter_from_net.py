import numpy as np
import cv2
def nothing(x):
    pass

cv2.namedWindow('image')
img = np.zeros((512,512,3),np.uint8)
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
drawing = False
mode = True
ix,iy = -1,-1

def drawing_fragment(event,x,y,flags,param):
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    color = (b,g,r)
    global drawing,ix,iy,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img,(ix,iy),(x,y),color,-1)
            else:
                cv2.circle(img,(x,y),5,color,-1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.setMouseCallback('image',drawing_fragment)
while True:
    cv2.imshow('image',img)
    k = cv2.waitKey(2)
    if k == 27:
        break
    elif k == ord('q'):
        mode = not mode
cv2.destroyAllWindows()
