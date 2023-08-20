import cv2 as cv
import numpy as np
two=[]
three=[]
four=[]
append=[]
input=[]
imglist=['photos/1.png']
dict={}


def colorchange(imglist):
    for i in imglist:
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
    valuelist=[RF, BF, RG, BG]
    return valuelist


def output(imglist):
    for i in imglist:
        final=values(i)
        #number of red houses on fire
        rf=final[0]
        #number of blue houses on fire
        bf=final[1]
        #number of red houses not on fire
        rg=final[2]
        #number of blue houses not on fire
        bg=final[3]
        name=i ##a passed as name of file in parameter of the function
        Hb=rf+bf
        Hg=rg+bg
        imglist2=[Hb, Hg]
        Pb=rf*1+bf*2
        Pg=rg*1+bg*2
        imglist3=[Pb, Pg]
        Pr=Pb/Pg
        results=[name, imglist2, imglist3, Pr]
        return results
def collectoutput(imglist):
    for i in imglist:
        x=output(i)
        two.append(x[1])
        three.append(x[2])
        four.append(x[3])
        dict[x[0]]=x[3]
        
print(dict) 

colorchange(imglist)
collectoutput(imglist)
print('2. ', two)
print('3. ', three)
print('4. ', four)
# Sorting the dictionary keys by values in descending order
sorted_keys = sorted(dict.keys(), key=lambda key: dict[key], reverse=True)
for key in sorted_keys:
    print(key)

def allcode(imglist):
    colorchange(imglist)
    collectoutput(imglist)

    


    



