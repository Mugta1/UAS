import cv2 as cv
import numpy as np
two=[]
three=[]
four=[]
dictxyz={}
#function for color change as asked in 1st question
def colorchange(i):
    img = cv.imread(i)
    brown_lower = np.array([10, 50, 50])
    brown_upper = np.array([30, 255, 255])
    green_lower = np.array([35, 50, 50])
    green_upper = np.array([85, 255, 255])
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    brown_mask = cv.inRange(hsv_img, brown_lower, brown_upper)
    green_mask = cv.inRange(hsv_img, green_lower, green_upper)
    yellow_color = np.array([60, 255, 255])
    img[np.where(brown_mask)] = yellow_color
    blue_color = np.array([120, 255, 255])
    img[np.where(green_mask)] = blue_color
    result_img = cv.cvtColor(img, cv.COLOR_HSV2BGR)
    blur=cv.bilateralFilter(result_img, 100,100,100)
    cv.imwrite('edited_img.jpg', blur)
    cv.imshow('Edited img', result_img)
    cv.waitKey(0)


#function for doing all the triangle visualization questions (2,3,4)
def values(i):
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
    #common cannys
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

    #total houses on fire
    HF=RF+BF
    #total houses on grass
    HG=RG+BG
    #priority of house on fire
    PF= (RF*1)+(BF*2)
    #priority of house on grass
    PG=(RG*1)+(BG*2)
    #priority ratio
    PR=PF/PG

    two.append([HF, HG])
    three.append([PF, PG])
    four.append(PR)
    dictxyz[i]=PR


#defining a final function that calculates everything

def final(i):
    colorchange(i)
    values(i)



final('photos/1.png')
final('photos/2.png')
final('photos/3.png')
final('photos/4.png')
final('photos/5.png')


print(two)
print(three)
print(four)
print(dictxyz)

sorted = sorted(dictxyz, key=dictxyz.get, reverse=True)

print(sorted)

