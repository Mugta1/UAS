import cv2 as cv
import numpy as np
imglist=['photos/1.png', 'photos/2.png', 'photos/3.png','photos/4.png', 'photos/5.png', 'photos/6.png', 'photos/7.png', 'photos/8.png', 'photos/10.png', 'photos//11.png']
#defining a function
def values(imglist):
    for i in imglist:
        img=cv.imread(i)
        bi=cv.bilateralFilter(img, 100, 100 ,100)
        b,g,r= cv.split(bi)
        retr, threshb=cv.threshold(b, 128, 255, cv.THRESH_BINARY)
        retr, threshr=cv.threshold(r, 128, 255, cv.THRESH_BINARY)

        #create masks for burnt and unburnt area

        hsv=cv.cvtColor(bi, cv.COLOR_BGR2HSV)
        LG=np.array([35,50,50])
        UG=np.array([85,255,255])

        #values of hsv used above were taken from findinghsv.py under meainscript folder in the repo
        #making masks
        greenmask=cv.inRange(hsv, LG, UG)

        kernel = np.ones((5,5), np.uint8)

        greenmask=cv.morphologyEx(greenmask, cv.MORPH_CLOSE, kernel)

        greenmask=cv.bitwise_not(greenmask)


        cannygrass=cv.Canny(greenmask, 125, 175 )
        cannyr=cv.Canny(threshr, 125, 175)
        cannyb=cv.Canny(threshb, 125, 175)

        commonrg=cv.bitwise_and(cannygrass, cannyr)
        commonbg=cv.bitwise_and(cannyb, cannygrass)
        ##calculating the number of blue and red houses
        contourR, heirarchies= cv.findContours(cannyr,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE )
        TR=int((len(contourR))/2)
        contourB, heirarchies= cv.findContours(cannyb,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE )
        TB=int((len(contourB))/2)

        #number of red houses not on fire
        contour1, heirarchies = cv.findContours(commonrg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        RG=int((len(contour1))/3)

        #number of blue houses not on fire
        contour2, heirarchies= cv.findContours(commonbg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        BG=int((len(contour2)/3))

        #number of red houses on fire
        RF=TR - RG

        #number of blue houses on fire
        BF=TB - BG

        ##printing the number of houses
        valuelist=[]
        return valuelist

        cv.waitKey(0)