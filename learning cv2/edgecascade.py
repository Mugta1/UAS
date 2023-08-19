import cv2 as cv
import numpy as np
img=cv.imread("photos/gow.png")
canny=cv.Canny(img, 125,175)
cv.imshow('edge', canny)

##apply blur to get rid of some of the edges

##dilating the image
dilated=cv.dilate(canny, (11,11), iterations=1)
cv.imshow('dilated', dilated)

##eroding
eroded=cv.erode(dilated, (3,3))
cv.imshow('eroded', eroded)
##resize
resized=cv.resize(img, (500,500))
cv.imshow('resized', resized)

##cropping
cropped=img[50:200, 200:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)
