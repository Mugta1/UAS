import cv2
import numpy as np

# Load the image
image_path = "photos/2.png"
image = cv2.imread(image_path)

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define color ranges for green and brown regions
green_lower = np.array([35, 50, 50])
green_upper = np.array([85, 255, 255])
brown_lower = np.array([0, 50, 50])
brown_upper = np.array([35, 255, 255])

# Create masks for green and brown regions
green_mask = cv2.inRange(hsv_image, green_lower, green_upper)
brown_mask = cv2.inRange(hsv_image, brown_lower, brown_upper)

# Define color ranges for red and blue houses
red_lower = np.array([0, 50, 50])
red_upper = np.array([10, 255, 255])
blue_lower = np.array([100, 50, 50])
blue_upper = np.array([130, 255, 255])

# Create masks for red and blue houses
red_mask = cv2.inRange(hsv_image, red_lower, red_upper)
blue_mask = cv2.inRange(hsv_image, blue_lower, blue_upper)

# Count blue and red houses in green region
green_blue_houses = cv2.countNonZero(blue_mask & green_mask)
green_red_houses = cv2.countNonZero(red_mask & green_mask)

# Count blue and red houses in brown region
brown_blue_houses = cv2.countNonZero(blue_mask & brown_mask)
brown_red_houses = cv2.countNonZero(red_mask & brown_mask)

# Print the results
print("Green Region:")
print("Blue Houses:", green_blue_houses)
print("Red Houses:", green_red_houses)

print("Brown Region:")
print("Blue Houses:", brown_blue_houses)
print("Red Houses:", brown_red_houses)
