A guide to this repository 
learning cv2- > contains all the codes written during the learning of cv2 library and numpy library from the date the task was given on.
misc-> contains codes that define functions that I have finally used in the final script.
photos-> contains all the photo data provided + some other data i used to make my program run (color images to find the hsv value of the colros for masking purposes, etc.)
videos-> audio visual data used to learn cv2, irrelevant to the task.
final script-> contains final.py, that is, the final script that is the answer to the task.







Image Processing Script README
Overview

This script performs various image processing tasks on a list of input images. It utilizes the OpenCV library and numpy to achieve color changes and analyze image features. The script contains several functions to achieve different tasks:

    a)colorchange(i): This function changes specific colors in an image based on their HSV values.

    b)values(i): This function processes an image to extract certain features, calculates the number of houses on fire, their priorities, and related values.

    c)final(i): This function combines the color change and values analysis functions for a given image.

    d)Main Loop: The script loops through a list of input images, applying the final(i) function to each image.

    e)Sorting: After processing, the script arranges the processed images based on their priority ratios and prints the results.


Output

The script outputs the following information for each input image:

    Number of houses on fire and total houses on grass: second list
    Priority of houses on fire and priority of houses on grass: third list
    Priority ratios: fourth list
    Sorted keys of images based on priority ratios: sortedkeys list





Working of individual functions:
    A) values()
        How it Works
            1.Read the image and apply bilateral filtering.
            2.Separate the image into blue, green, and red channels.
            3.Apply thresholding to the blue and red channels to create masks.
            4.Convert the image to the HSV color space and create a mask for grass areas.
            5.Apply morphological operations to the grass mask.
            6.Use edge detection (Canny) to detect edges in the grass, blue, and red masks.
            7.Calculate common regions between the edge maps to identify houses.
            8.Count the number of red and blue houses on fire and not on fire.
            9.Calculate the total number of houses on fire and on grass.
            10.Compute priority scores for houses on fire and on grass.
            11.Calculate the priority ratio based on the priority scores.
        Note
            The: HSV thresholding values (LG and UG) are assumed to be determined in advance and are referenced from a script named findinghsv.py.



    B)colorchange()
        The script performs the following steps for each image:

            1.Read the image.
            2.Define color ranges for the colors you want to enhance (brown and green).
            3.Convert the image to the HSV color space.
            4. Create masks for the brown and green colors based on the specified color ranges.
            5.Replace pixels within the brown mask with a yellow color, enhancing brown areas.
            6.Replace pixels within the green mask with a blue color, enhancing green areas.
            7.Convert the HSV-edited image back to the BGR color space.
            8.Display the enhanced image for visualization.