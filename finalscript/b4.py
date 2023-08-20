import cv2 as cv
import numpy as np
img=cv.imread('photos/11.png')
cv.imshow('og', img)

bi=cv.bilateralFilter(img, 100, 100 ,100)
b,g,r= cv.split(bi)
retr, threshb=cv.threshold(b, 128, 255, cv.THRESH_BINARY)
retr, threshr=cv.threshold(r, 128, 255, cv.THRESH_BINARY)

#create masks for burnt and unburnt area

hsv=cv.cvtColor(bi, cv.COLOR_BGR2HSV)
LB=np.array([10,50,50])
UB=np.array([30,255,255])
LG=np.array([35,50,50])
UG=np.array([85,255,255])

#values of hsv used above were taken from findinghsv.py under meainscript folder in the repo

#making masks
burntmask=cv.inRange(hsv, LB, UB)
greenmask=cv.inRange(hsv, LG, UG)

kernel = np.ones((5,5), np.uint8)
burntmask=cv.morphologyEx(burntmask, cv.MORPH_CLOSE, kernel)
greenmask=cv.morphologyEx(greenmask, cv.MORPH_CLOSE, kernel)
burntmask=cv.bitwise_not(burntmask)
greenmask=cv.bitwise_not(greenmask)
burntmask=cv.GaussianBlur(burntmask, (17,17), 0)
cannybr=cv.GaussianBlur(burntmask, (7,7), cv.BORDER_DEFAULT)
cannygr=cv.Canny(greenmask, 125, 175 )
cannybr=cv.Canny(cannybr, 125, 175)
cannyr=cv.Canny(threshr, 125, 175)
cannyb=cv.Canny(threshb, 125, 175)

commonrg=cv.bitwise_and(cannygr, cannyr)
commonrb=cv.bitwise_and(cannybr, cannyr)

""" cv.imshow('cannyb', cannyb)
cv.imshow('cannybr', cannybr)
cv.imshow('commonrg', commonrg)
cv.imshow('cannyr', cannyr)
cv.imshow('commonrb', commonrb) """
commonrb=cv.dilate(commonrg, (501,501), iterations=1)
contour, heirarchies = cv.findContours(commonrg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
n=(len(contour))/3
#cv.imshow('final', commonrg)
print(n)
cv.waitKey(0)