import cv2
import numpy as np

# Load the image
image = cv2.imread('photos/3.png')

# Convert the image to the HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# Define color ranges for the brown and green areas
brown_lower = np.array([10, 50, 50])
brown_upper = np.array([30, 255, 255])

green_lower = np.array([35, 50, 50])
green_upper = np.array([85, 255, 255])

# Create masks for the brown and green areas
brown_mask = cv2.inRange(hsv_image, brown_lower, brown_upper)
green_mask = cv2.inRange(hsv_image, green_lower, green_upper)

# Apply morphological operations to clean up the masks
kernel = np.ones((5, 5), np.uint8)
brown_mask = cv2.morphologyEx(brown_mask, cv2.MORPH_CLOSE, kernel)
green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_CLOSE, kernel)

# Separate the houses in the brown and green areas
houses_brown = cv2.bitwise_and(image, image, mask=brown_mask)
houses_green = cv2.bitwise_and(image, image, mask=green_mask)
cv2.imshow('greenmask', green_mask)
cv2.imshow('brown', brown_mask)
# Display the images with houses in the brown and green areas
cv2.imshow('Houses in Brown Area', houses_brown)
cv2.imshow('Houses in Green Area', houses_green)

cv2.waitKey(0)
cv2.destroyAllWindows()
