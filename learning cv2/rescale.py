import cv2 as cv
img= cv.imread('photos\gow.png')

def rescaleFrame(frame, scale):
    width=int(frame.shape[0]*scale)
    length=int(frame.shape[1]*scale)
    dimensions=(width,length)
    return cv.resize(frame,dimensions)
xyz=rescaleFrame(img, 0.1)
cv.imshow('gow', img)
cv.imshow('xyz', xyz)
cv.waitKey(0)