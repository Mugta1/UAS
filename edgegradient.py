import cv2 as cv
import numpy as np
img=cv.imread('photos/1.png')
cv.imshow('img', img)
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#laplacian
lap=cv.Laplacian(gray, cv.CV_64F)
lap=np.uint8(np.absolute(lap))
#sobel
sobelx= cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely= cv.Sobel(gray, cv.CV_64F, 0, 1)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
bitwiseor=cv.bitwise_or(sobelx, sobely)
cv.imshow('bit',bitwiseor)
cv.imshow('lap', lap)
cv.waitKey(0)