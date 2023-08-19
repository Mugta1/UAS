import cv2 as cv
import numpy as np
two=[]
three=[]
four=[]
append=[]
input=[]
def colorchange(list):
    for i in list:
        img = cv.imread(a)  # Replace with the actual path of your img
        cv.imshow('img', img)
        # Define the color ranges for brown and green in HSV
        brown_lower = np.array([10, 50, 50])
        brown_upper = np.array([30, 255, 255])
        green_lower = np.array([35, 50, 50])
        green_upper = np.array([85, 255, 255])

        # Convert the img to the HSV color space
        hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        # Create masks for brown and green parts
        brown_mask = cv.inRange(hsv_img, brown_lower, brown_upper)
        green_mask = cv.inRange(hsv_img, green_lower, green_upper)

        # Convert brown parts to neon yellow
        yellow_color = np.array([60, 255, 255])
        img[np.where(brown_mask)] = yellow_color

        # Convert green parts to neon blue
        blue_color = np.array([120, 255, 255])
        img[np.where(green_mask)] = blue_color

        # Convert the img back to BGR color space
        result_img = cv.cvtColor(img, cv.COLOR_HSV2BGR)
        blur=cv.bilateralFilter(result_img, 100,100,100)
        # Save the edited img
        cv.imwrite('edited_img.jpg', blur)

        # Display the edited img (optional)
        cv.imshow('Edited img', result_img)
        cv.waitKey(0)
        cv.destroyAllWindows()

def output(a):
    #try1.py will return values
    #number of red houses on fire
    rf=4
    #number of blue houses on fire
    bf=2
    #number of red houses not on fire
    rg=1
    #number of blue houses not on fire
    bg=3
    name=a ##a passed as name of file in parameter of the function
    Hb=rf+bf
    Hg=rg+bg
    list2=[Hb, Hg]
    Pb=rf*1+bf*2
    Pg=rg*1+bg*2
    list3=[Pb, Pg]
    Pr=Pb/Pg
    results=[name, list2, list3, Pr]
    return results
def collectoutput(list):
    for i in list:
        x=output(i)
        two.append(x[1])
        three.append(x[2])
        four.append(x[3])
        input.append([x[0], x[3]])
def get_float(pair):
    return pair[1]

def arrange_by_float_descending(input):
    sorted_pairs = sorted(input, key=get_float, reverse=True)
    return sorted_pairs
colorchange(list)
collectoutput(list)
print('2. ', two)
print('3. ', three)
print('4. ', four)
sorted_output = arrange_by_float_descending(input)

for name, value in sorted_output:
    print(f"{name}")

    



