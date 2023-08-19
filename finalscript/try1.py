import cv2 as cv
import numpy as np
img=cv.imread('photos/3.png')


##creating a layer of just houses(separated by blue and red)


bi=cv.bilateralFilter(img, 50, 100 ,100)
b,g,r= cv.split(bi)
retr, threshb=cv.threshold(b, 128, 255, cv.THRESH_BINARY_INV)
retr, threshr=cv.threshold(r, 128, 255, cv.THRESH_BINARY_INV)

#create masks for burnt and unburnt area

hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
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
cv.imshow('burn', burntmask)
cv.imshow('green', greenmask)
cv.imshow('threshr', threshr)
#for burnt region
burntmask_resized = cv.resize(burntmask, (img.shape[1], img.shape[0]))
threshr_resized = cv.resize(threshr, (img.shape[1], img.shape[0]))

# Find the common regions using bitwise AND
common_mask = cv.bitwise_and(burntmask_resized, threshr_resized)

# Display the common regions
cv.imshow('Common Regions', common_mask)
##this is the error-d region, bitwise_and is giving union instead of intersection.


cv.waitKey(0)