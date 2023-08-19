import cv2 as cv
import numpy as np
img=cv.imread('photos/ref.png')
cv.imshow('new', img)

cv.waitKey(0)