A guide to this repository 
learning cv2- > contains all the codes written during the learning of cv2 library and numpy library from the date the task was given on.
misc-> contains codes that define functions that I have finally used in the final script.
photos-> contains all the photo data provided + some other data i used to make my program run (color images to find the hsv value of the colros for masking purposes, etc.)
videos-> audio visual data used to learn cv2, irrelevant to the task.
final script-> contains final.py, that is, the final script that is the answer to the task.






WORKINGS OF ALL THE FUNCTIOSN
Image Processing Script README
Overview

This script performs various image processing tasks on a list of input images. It utilizes the OpenCV library and numpy to achieve color changes and analyze image features. The script contains several functions to achieve different tasks:

    colorchange(i): This function changes specific colors in an image based on their HSV values.

    values(i): This function processes an image to extract certain features, calculates the number of houses on fire, their priorities, and related values.

    final(i): This function combines the color change and values analysis functions for a given image.

    Main Loop: The script loops through a list of input images, applying the final(i) function to each image.

    Sorting: After processing, the script arranges the processed images based on their priority ratios and prints the results.


Output

The script outputs the following information for each input image:

    Number of houses on fire and total houses on grass: second list
    Priority of houses on fire and priority of houses on grass: third list
    Priority ratios: fourth list
    Sorted keys of images based on priority ratios: sortedkeys list





Working of individual functions:
    values()
        How it Works
            Read the image and apply bilateral filtering.
            Separate the image into blue, green, and red channels.
            Apply thresholding to the blue and red channels to create masks.
            Convert the image to the HSV color space and create a mask for grass areas.
            Apply morphological operations to the grass mask.
            Use edge detection (Canny) to detect edges in the grass, blue, and red masks.
            Calculate common regions between the edge maps to identify houses.
            Count the number of red and blue houses on fire and not on fire.
            Calculate the total number of houses on fire and on grass.
            Compute priority scores for houses on fire and on grass.
            Calculate the priority ratio based on the priority scores.
        Note
            The HSV thresholding values (LG and UG) are assumed to be determined in advance and are referenced from a script named findinghsv.py.



    colorchange()
        The script performs the following steps for each image:

            Read the image.
            Define color ranges for the colors you want to enhance (brown and green).
            Convert the image to the HSV color space.
            Create masks for the brown and green colors based on the specified color ranges.
            Replace pixels within the brown mask with a yellow color, enhancing brown areas.
            Replace pixels within the green mask with a blue color, enhancing green areas.
            Convert the HSV-edited image back to the BGR color space.
            Display the enhanced image for visualization.

        Note

            The script modifies specific colors (brown and green) based on the defined color ranges.
            The enhanced images are displayed after processing, allowing you to visually inspect the changes made.