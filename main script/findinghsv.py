import cv2 as cv
import numpy as np
green=cv.imread('photos/blue.png')
hsvGreen=cv.cvtColor(green, cv.COLOR_BGR2HSV)
lowerG = hsvGreen[0][0][0] - 10, 100, 100
upperG = hsvGreen[0][0][0] + 10, 255, 255
brown=cv.imread('photos/yellow.png')
hsvBrown=cv.cvtColor(brown, cv.COLOR_BGR2HSV)
lowerB = hsvBrown[0][0][0] - 10, 100, 100
upperB = hsvBrown[0][0][0] + 10, 255, 255
print("lowerg", lowerG)
print("upperg", upperG)
print('lowerb', lowerB)
print('upperb', upperB)
cv.waitKey(0)