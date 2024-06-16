# Fire and House Priority Detection using OpenCV

## Index
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Script Explanation](#script-explanation)
    - [colorchange(i)](#colorchangei)
    - [values(i)](#valuesi)
    - [final(i)](#finali)
7. [Output](#output)
8. [Example](#example)
9. [License](#license)
10. [Acknowledgements](#acknowledgements)

## Introduction

This project focuses on detecting and prioritizing red and blue houses in aerial images, distinguishing between those that are on fire (brown areas) and those that are safe on grass (green areas). Using OpenCV and Python, the program processes images to highlight areas of interest, classify the houses, and assign rescue priorities based on their color and condition. Blue houses have a higher priority than red ones, with an added emphasis on those that are on fire.

## Features
- **Color Change**: Converts brown areas to yellow and green areas to blue in the provided images for better visualization.
- **House Detection and Classification**: Detects houses and classifies them based on color (red or blue) and state (on fire or on grass).
- **Priority Calculation**: Assigns rescue priorities based on the number and condition of the houses.
- **Sorting**: Sorts the images based on the calculated rescue priority for efficient response planning.

## Prerequisites
- Python 3.x
- OpenCV
- NumPy

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mugta1/UAS-1.git
   cd UAS-1
   ```

2. Install the required libraries:
   ```bash
   pip install numpy opencv-python
   ```

## Usage
1. Place your images in the `photos` directory.
2. Run the script:
   ```bash
   python final.py
   ```

## Script Explanation

### `colorchange(i)`
- **Purpose**: Modifies the colors in the image to enhance visualization by converting brown areas to yellow and green areas to blue.
- **Parameters**: 
  - `i`: Path to the input image.
- **Process**:
  1. Reads the image and converts it from BGR to HSV color space.
  2. Creates masks to detect brown and green areas using predefined HSV color ranges.
  3. Changes the color of detected brown areas to yellow and green areas to blue.
  4. Converts the modified HSV image back to BGR color space.
  5. Displays the edited image using OpenCV's `imshow` function.

### `values(i)`
- **Purpose**: Detects houses, determines if they are on fire or not, and calculates various metrics related to house priority for rescue.
- **Parameters**: 
  - `i`: Path to the input image.
- **Process**:
  1. Reads the image and applies a bilateral filter for noise reduction.
  2. Splits the image into its BGR components and applies binary thresholding.
  3. Creates a mask to detect green areas, representing unburnt regions.
  4. Performs morphological transformations on the green mask and inverts it to identify non-green areas.
  5. Uses the Canny edge detector to find edges in the green mask and thresholded images.
  6. Identifies contours in the edge-detected images to count the number of red and blue houses.
  7. Calculates the number of red and blue houses on fire and on grass.
  8. Computes total houses on fire, total houses on grass, and assigns rescue priorities.
  9. Appends the calculated values to respective lists and dictionaries for further use.


### `final(i)`
- **Purpose**: Combines the `colorchange` and `values` functions to fully process each image.
- **Parameters**: 
  - `i`: Path to the input image.
- **Process**:
  1. Calls the `colorchange` function to modify the colors in the image.
  2. Calls the `values` function to detect houses and calculate metrics.
  3. Closes all OpenCV windows after processing.
- **Code**:
  ```python
  def final(i):
      colorchange(i)
      values(i)
      cv.destroyAllWindows()
  ```

### Main Script
- **Process**:
  1. Defines a list of image paths to be processed.
  2. Iterates over each image path, calling the `final` function to process each image.
  3. Sorts the images based on the priority ratios calculated in the `values` function.
  4. Prints the results for total houses on fire and on grass, priority values, priority ratios, and the sorted list of image paths.
- **Code**:
  ```python
  imglist = ['photos/1.png', 'photos/2.png', 'photos/3.png', 'photos/4.png', 'photos/5.png', 
             'photos/6.png', 'photos/7.png', 'photos/8.png', 'photos/10.png', 'photos/11.png']

  for i in imglist:
      final(i)

  sortedkeys = sorted(dictxyz, key=dictxyz.get, reverse=True)
  print('2.', second)
  print('3.', third)
  print('4.', fourth)
  print('5.', sortedkeys)
  ```

## Output
- **Second Output**: List of total houses on fire and on grass for each image.
- **Third Output**: List of priority values for houses on fire and on grass for each image.
- **Fourth Output**: List of priority ratios for each image.
- **Fifth Output**: Sorted list of image paths based on the priority ratios.

## Example
```python
# Output Example
2. [[1, 2], [2, 3], ...]
3. [[1, 4], [3, 

5], ...]
4. [0.5, 0.6, ...]
5. ['photos/2.png', 'photos/5.png', ...]

```
## Contributions

Feel free to contribute to this project by forking the repository and submitting pull requests!

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Mugta1/UAS-1/blob/main/LICENSE) file for details.

## Acknowledgements
- **OpenCV**: For providing extensive documentation and tutorials which were instrumental in developing the image processing components of this project.
- **NumPy**: For its powerful array manipulation capabilities which facilitated the handling of image data.
- **Python**: For being the versatile programming language that made this project possible.


