import cv2
import numpy as np

# Load the image
image = cv2.imread('photos/ref.png')

# Define color ranges for the blue region
blue_lower = np.array([80, 100, 100])
blue_upper = np.array([100, 255, 255])

# Create a mask for the blue region
blue_mask = cv2.inRange(image, blue_lower, blue_upper)
cv2.imshow('mask', blue_mask)

# Apply morphological operations to clean up the mask
kernel = np.ones((5, 5), np.uint8)
blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_CLOSE, kernel)

# Create an image with only the blue region and its components
blue_region = cv2.bitwise_and(image, image, mask=blue_mask)

# Show the image with only the blue region
cv2.imshow('Blue Region Image', blue_region)
cv2.waitKey(0)
cv2.destroyAllWindows()