import cv2 as cv
import numpy as np
img=cv.imread("photos/gow.png", 0)
cv.imshow("img", img)
canny= cv.Canny(img, 125, 175)
dilated=cv.dilate(canny, (11,11), iterations=1)

contour, heirarchies= cv.findContours(dilated, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

cv.waitKey(0)