import cv2 as cv
import numpy as np

# Load the image
image = cv.imread('photos/3.png')
bi=cv.bilateralFilter(image, 50,100,100)
# Convert the image to the HSV color space
hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)


# Define color ranges for the brown and green areas
brown_lower = np.array([10, 50, 50])
brown_upper = np.array([30, 255, 255])

green_lower = np.array([35, 50, 50])
green_upper = np.array([85, 255, 255])

# Create masks for the brown and green areas
brown_mask = cv.inRange(hsv_image, brown_lower, brown_upper)
green_mask = cv.inRange(hsv_image, green_lower, green_upper)

# Apply morphological operations to clean up the masks
kernel = np.ones((5, 5), np.uint8)
brown_mask = cv.morphologyEx(brown_mask, cv.MORPH_CLOSE, kernel)
green_mask = cv.morphologyEx(green_mask, cv.MORPH_CLOSE, kernel)

# Separate the houses in the brown and green areas
houses_brown = cv.bitwise_and(image, image, mask=brown_mask)
houses_green = cv.bitwise_and(image, image, mask=green_mask)
cv.imshow('greenmask', green_mask)
cv.imshow('brown', brown_mask)
# Display the images with houses in the brown and green areas
cv.imshow('Houses in Brown Area', houses_brown)
cv.imshow('Houses in Green Area', houses_green)

blur=cv.bilateralFilter(houses_brown, 25,50,50)
canny=cv.Canny(blur, 125,175)
contours, heirarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
n=len(contours)
cv.imshow('canny', canny)
b,g,r= cv.split(image)
retr, threshb=cv.threshold(b, 128, 255, cv.THRESH_BINARY)
retr, threshr=cv.threshold(r, 128, 255, cv.THRESH_BINARY)
threshr=cv.GaussianBlur(threshr, (3,3), cv.BORDER_DEFAULT)
threshr=cv.bilateralFilter(threshr, 50,100,100)
cv.imshow('retr', threshr)
blank=np.zeros(image.shape[:2], dtype='uint8')
canny2=cv.Canny(bi, 125,175)
cv.imshow('ogcontour', canny2)

print(n)
cv.waitKey(0)
cv.destroyAllWindows()
