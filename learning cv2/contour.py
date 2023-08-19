import cv2 as cv
import numpy as np
img=cv.imread("photos/1.png", 0)
cv.imshow("img", img)
canny= cv.Canny(img, 125, 225)
dilated=cv.dilate(canny, (11,11), iterations=1)
blur=cv.GaussianBlur(dilated, (3,3), cv.BORDER_DEFAULT )
cv.imshow("god", dilated)
contour, heirarchies= cv.findContours((dilated), cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contour))
blank=np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contour, 1500, (0,0,255),2)
cv.imshow('contour drawn', blank)
cv.waitKey(0)
##len(contour) for canny is 1509
##len(Contour) for dilated is 2936
##len(contour) for blur is 756