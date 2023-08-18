import cv2 as cv
import numpy as np
img=cv.imread('photos/gow.png')

cv.imshow("img", img)

##Translation
def translate(img, x, y):
    transMat= np.float32([[1,0,x],[0,1,y]])
    dimensions= (img.shape[1], img.shape[2])
    return cv.warpAffine(img, transMat, dimensions)
##-x= left
##-y= up
##x= right
##y= down
translated= translate(img, -1, 2)
cv.imshow('ttr', translated)
cv.waitKey(0)
