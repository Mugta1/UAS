import cv2 as cv
img=cv.imread('photos/gow.png', 0) 
cv.imshow('img', img)
cv.waitKey(0)

##adding zero as secondary parameter makes the img b&w