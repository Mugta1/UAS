import cv2 as cv
import numpy as np
img=cv.imread("photos/1.png")
cv.imshow("img", img)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
canny= cv.Canny(blur, 125, 225)
cv.imshow('nlur', blur)
dilated=cv.dilate(img, (7,7), iterations=1)
contour, heirarchies= cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
blank=cv.imread("photos/blank.png")
cv.drawContours(blank, contour, -1, (0,255,0),1)
cv.imshow('contour drawn', blank)
cv.waitKey(0)
