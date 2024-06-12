A guide to this repository 
learning cv2- > contains all the codes written during the learning of cv2 library and numpy library 
misc-> contains codes that define functions that I have finally used in the final script.
photos-> contains all the photo data provided + some other data i used to make my program run (color images to find the hsv value of the colros for masking purposes, etc.)
videos-> audio visual data used to learn cv2, irrelevant to the task.
final script-> contains final.py, that is, the final script for the project mentioned below


# Project ReadMe

## Overview

This project focuses on advanced image processing techniques to analyze the condition of houses in a given set of images. The code applies sophisticated color transformations, image filtering, and contour detection algorithms to compute various metrics related to the state of the houses (e.g., on fire, on grass). The results are utilized to determine the priority for addressing houses on fire, providing a systematic approach to crisis management.

## Prerequisites

Ensure you have the following dependencies installed before running the code:

- Python 3.x
- OpenCV (`cv2`) library
- NumPy library

You can install the required libraries using the following commands:

```bash
pip install opencv-python
pip install numpy
```

## Input Data

The program processes a list of image file paths. The images should be located in a directory named `photos`.

## Code Description

### Functions

1. **colorchange(i)**

   This function performs targeted color transformations within the image:
   - Converts brown areas (indicative of burnt regions) to yellow.
   - Converts green areas (indicative of grass) to blue.

   The transformation leverages the HSV color space for accurate color thresholding:
   - Brown areas: Defined by HSV ranges `[10, 50, 50]` to `[30, 255, 255]`.
   - Green areas: Defined by HSV ranges `[35, 50, 50]` to `[85, 255, 255]`.

   The modified image is then displayed using OpenCV.

2. **values(i)**

   This function executes a series of image processing steps to identify and quantify houses:
   - Applies a bilateral filter to reduce noise while preserving edges.
   - Splits the image into its blue, green, and red channels.
   - Creates binary thresholds for the blue and red channels to isolate houses.
   - Constructs a mask for green areas (unburnt grass) using HSV color space thresholds.
   - Identifies contours for houses based on color segmentation:
     - Red for houses on fire.
     - Blue for houses not on fire.
   - Computes the number of houses on fire, houses on grass, and their respective priorities:
     - `HF` (Houses on Fire)
     - `HG` (Houses on Grass)
     - `PF` (Priority of Fire)
     - `PG` (Priority of Grass)
     - `PR` (Priority Ratio)

   Results are stored in global lists and a dictionary for further analysis.

3. **final(i)**

   This function integrates `colorchange` and `values` to process each image in the list. It ensures proper handling of OpenCV windows.

### Main Script

The main script iterates over a predefined list of image file paths, invoking the `final(i)` function for each image. After processing all images, it sorts the results based on the computed priority ratios and prints the comprehensive results.

## Output

The output consists of several technical metrics printed to the console:

1. **List of houses on fire and houses on grass for each image:**

   ```python
   [[HF1, HG1], [HF2, HG2], ..., [HFn, HGn]]
   ```

2. **List of priority values for houses on fire and houses on grass for each image:**

   ```python
   [[PF1, PG1], [PF2, PG2], ..., [PFn, PGn]]
   ```

3. **List of priority ratios for each image:**

   ```python
   [PR1, PR2, ..., PRn]
   ```

4. **Sorted list of image file paths based on priority ratio in descending order:**

   ```python
   ['photos/2.png', 'photos/

1.png', ..., 'photos/10.png']
   ```

Where:
- `HF` (Houses on Fire)
- `HG` (Houses on Grass)
- `PF` (Priority of Fire)
- `PG` (Priority of Grass)
- `PR` (Priority Ratio)

## Usage

To execute the script, run the Python file in your environment. Ensure that the images are correctly placed in the `photos` directory.

```bash
python script.py
```

The script will process each image, apply the necessary color changes, compute the required metrics, and display the results.

## Detailed Example

Given a list of images:

```python
imglist = ['photos/1.png', 'photos/2.png', 'photos/3.png', 'photos/4.png', 'photos/5.png', 'photos/6.png', 'photos/7.png', 'photos/8.png', 'photos/10.png', 'photos/11.png']
```

The script will:

1. Apply the color transformations to highlight specific areas (burnt regions to yellow, grass to blue).
2. Perform image processing to detect and count houses:
   - Identify red houses (indicative of being on fire).
   - Identify blue houses (indicative of being safe).
   - Determine the number of houses on grass and on fire.
   - Compute priority metrics to assist in crisis management.
3. Output the results in a structured format, including sorted priorities for targeted intervention.

## Implementation Notes

- Ensure images are in the correct format and located in the specified directory.
- The HSV color thresholds used for color detection are based on empirical values and may require adjustments for different datasets.
- OpenCV windows displaying the processed images need to be manually closed to proceed.

## Conclusion

This project demonstrates the application of advanced image processing techniques to analyze and prioritize houses based on their condition (on fire or on grass). The structured output provides valuable insights for effective crisis management, ensuring that houses on fire are addressed with the appropriate priority. This systematic approach is backed by comprehensive image analysis, making it robust for real-world applications.
