import numpy as np
import cv2 as cv
###reading images
'''img= cv.imread('photos\gow.png')
cv.imshow('gow', img)'''

## reading videos
vid=cv.VideoCapture("D:/python/videos/God of War 2023.07.23 - 21.12.01.02.DVR.mp4")
while True:
    isTrue, frame = vid.read()
    cv.imshow('vid', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
vid.release
cv.destroyAllWindows()
