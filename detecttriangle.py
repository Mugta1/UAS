import cv2 as cv
import numpy as np
img=cv.imread("photos/11.png")

bi=cv.bilateralFilter(img, 50, 100, 100)
cv.imshow('c',bi)

canny=cv.Canny(bi, 125,175)
blur=cv.GaussianBlur(canny, (3,3), cv.BORDER_DEFAULT)
contour, heirarchies= cv.findContours(blur, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
n=len(contour)
cv.imshow('canny', blur)
print(n)
cv.waitKey(0)