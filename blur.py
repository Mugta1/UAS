import cv2 as cv
import numpy as np
img=cv.imread("photos/gow.png")
blur=cv.GaussianBlur(img, (11,11), cv.BORDER_DEFAULT)
cv.imshow('img', img)
cv.imshow('blur', blur)
cv.waitKey(0)
