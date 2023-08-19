import cv2 as cv
import numpy as np
img= cv.imread('photos/gow.png',0)

threshold, thresh=cv.threshold(img, 150, 255, cv.THRESH_BINARY)
#adaptive thresholding
adaptive_thresh=cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 3)
cv.imshow('adaptive', adaptive_thresh)
cv.imshow('thresh', thresh)
cv.waitKey(0)