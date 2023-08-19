import cv2 as cv
import numpy as np
img=cv.imread('photos/2.png')
b,g,r=cv.split(img)
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)
cv.waitKey(0)