# OpenCV Color Analysis and Manipulation

Explore a curated collection of Python scripts and modules designed for advanced color analysis and pixel manipulation using OpenCV. 
This repository includes tools for capturing pixel values from a webcam, converting them into various formats, and applying color masks(binary masking) for precise color detection.

## Overview

This repository offers tools for pixel value capture, conversion, and color detection through masking. Whether you need to analyze colors interactively or apply precise color detection in real-time, these modules provide a versatile set of functionalities for your OpenCV projects.

## Modules

### 1. Pixel Value Capture Script (get_pixel_hsv_value.py)

This script opens a connection to the default webcam, captures the video feed, and enables users to click on the displayed frame to obtain the HSV value of the pixel at the clicked location. The script continuously displays the video feed, prints the HSV value in the console when the left mouse button is clicked, and appends these values to a list. After exiting from the video loop by pressing the 'q' key, the upper and lower bounds for that range of HSV pixel values are printed to the console for binary masking use.

Additionally, a function `get_thresh_from_vals` has been added to calculate the minimum and maximum values for each channel of the captured HSV pixel values and provide the lower and upper bounds for binary masking.

- **Usage:**
  - Ensure you have OpenCV installed (`pip install opencv-python`).
  - Run the script, click on the displayed frame to obtain HSV values, and press 'q' to exit the video loop and get the threshold values.


Updated: 1/11/2024

### 2. PixelConverter Class (pixel_converter.py)

The PixelConverter class provides functionality to capture pixel values from an OpenCV video feed and convert them into various formats such as BGR, RGB, Hex, HSV, and RGBA.

- **Usage:**
  - Import the `PixelConverter` class into your project.
  - Create an instance and run the `get_webcam_pixels` method to interactively capture pixel values.

- **Features:**
  - Conversion of pixel values into various formats.
  - Modular and object-oriented design for seamless integration.
  - Ideal for applications requiring color analysis and real-time interactive pixel insights.

- **Example:**
  ```python
  from pixel_converter import PixelConverter

  if __name__ == "__main__":
      pixel_converter = PixelConverter()
      pixel_converter.get_webcam_pixels()

### 3. Color Detector Module (color_detector.py)

The `ColorDetector` module enhances your OpenCV projects by providing a powerful tool for real-time color detection through masking. 
Whether you're identifying specific objects or exploring visual effects, this module allows you to dynamically choose color masks, from a set of 
pre-defined HSV-value ranges for masking specific colors, during runtime, providing flexibility and interactivity.


**Usage:**
- Import the `ColorDetector` class into your project.
- Create an instance and run the `run` method to start the `ColorDetector` application.

**Features:**
- Customizable color masking for various predefined colors.
- Real-time application, capturing video feed, applying color masks, and displaying results.

**User Input:**
- During runtime, press the 'c' key to dynamically choose the color mask from a list of predefined colors.

**Example:**
```python
from color_detector import ColorDetector

if __name__ == "__main__":
    color_detector = ColorDetector()
    color_detector.run()
```

## Author
Jacob Pitsenberger

## License
This software is licensed under the MIT License. By using this software, you agree to comply with the terms outlined in the license.