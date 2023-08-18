import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img=cv.imread("photos/1.png")
rgb= cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)
blur= cv.GaussianBlur(rgb,(3,3), cv.BORDER_DEFAULT)
canny=cv.Canny(blur, 125, 225)
contour, heirarchies= cv.findContours(canny,cv.RETR_TREE ,cv.CHAIN_APPROX_SIMPLE)
blank=cv.imread('photos/blank.png')
cv.drawContours(blank, contour,-1,(0,255,0), 1)
cv.imshow('blank', blank)
cv.waitKey(0)