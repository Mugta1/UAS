import cv2 as cv
import numpy as np
img=cv.imread('photos/3.png')

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
cannygr=cv.Canny(greenmask, 125, 175 )
cannybr=cv.Canny(burntmask, 125, 175)
cannyr=cv.Canny(threshr, 125, 175)
cannyb=cv.Canny(threshb, 125, 175)
commonrg=cv.bitwise_and(cannygr, cannyr)
commonrb=cv.bitwise_and(cannybr, cannyr)

cv.imshow('cannyg', cannygr)
cv.imshow('cannyr', cannyr)
cv.imshow('cannybr', cannybr)
cv.imshow('cannyb', cannyb)
cv.imshow('commonrg', commonrg)
cv.imshow('commonrb', commonrb)
commonrb=cv.dilate(commonrb, (501,501), iterations=1)
commonrb=cv.bilateralFilter(commonrb, 100, 100,100)
cv.imshow('final', commonrb)
contour, heirarchies = cv.findContours(commonrb, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
blank=np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('balnk', blank)

cv.drawContours(blank, contour, -1, (0, 255, 0), 3)
# Display the image with completed lines
cv.imshow("Image with Completed Lines", blank)



# Display the common regions





cv.waitKey(0)
