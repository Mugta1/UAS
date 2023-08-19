import cv2 as cv
import numpy as np
img=cv.imread('photos/2.png')
cv.imshow('og', img)
b,g,r=cv.split(img)
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)
canny=cv.Canny(g, 125, 225)
cv.imshow('canny', canny)

cv.waitKey(0)