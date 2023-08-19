import cv2 as cv
import numpy as np
img=cv.imread("photos/1.png")
rgb=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', rgb)
blur=cv.GaussianBlur( rgb, (7,7), cv.BORDER_DEFAULT)
contour=cv.Canny(blur, 125, 225)
cv.imshow('contour', contour)
contour, hierarchies= cv.findContours(contour, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE )
blank=cv.imread("photos/blank.png")
cv.drawContours(blank, contour, -1, (0,255,0),1)
cv.imshow('contour drawn', blank)
cv.waitKey(0)