import cv2 as cv
import numpy as np
two=[]
three=[]
four=[]
append=[]
input=[]
imglist=['photos/1.png', 'photos/2.png', 'photos/3.png','photos/4.png', 'photos/5.png', 'photos/6.png', 'photos/7.png', 'photos/8.png', 'photos/10.png', 'photos//11.png']
dict={}
def colorchange(imglist):
    for i in imglist:
        img = cv.imread(i)
        cv.imshow('img', img)
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

def output(imglist):
    for i in imglist:
        #try1.py will return values
        #number of red houses on fire
        rf=4
        #number of blue houses on fire
        bf=2
        #number of red houses not on fire
        rg=1
        #number of blue houses not on fire
        bg=3
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



    



