import cv2 as cv
import numpy as np
img=cv.imread("photos/gow.png")
cv.imshow("img", img)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
canny= cv.Canny(gray, 125, 225)
dilated=cv.dilate(canny, (11,11), iterations=1)
contour, heirarchies= cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contour, -1, (0,0,255),3)
cv.imshow('contour drawn', img)
cv.waitKey(0)
