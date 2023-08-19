import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread("photos/1.png")
rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)
blur= cv.GaussianBlur(rgb,(3,3), cv.BORDER_DEFAULT)
canny=cv.Canny(blur, 125, 225)
contour, heirarchies= cv.findContours(canny,cv.RETR_TREE ,cv.CHAIN_APPROX_NONE)
blank=cv.imread('photos/blank.png')
cv.drawContours(blank, contour,-1,(0,255,0), 1)
ret, thresh= cv.threshold(blank, 150, 255, cv.THRESH_BINARY)
cv.imshow('blank', blank)
cv.imshow('thresh', thresh)
cv.waitKey(0)