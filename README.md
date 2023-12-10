# OpenCV Color Analysis and Manipulation

Discover a curated collection of Python scripts and modules crafted for advanced color analysis and pixel manipulation using OpenCV.

## Modules

### 1. Pixel Value Capture Script

This script opens a connection to the default webcam, captures the video feed, and allows the user to click on the displayed frame to obtain the HSV value of the pixel at the clicked location. The script continuously displays the video feed and prints the HSV value in the console when the left mouse button is clicked.

- **Usage:**
  - Ensure you have OpenCV installed (`pip install opencv-python`).
  - Run the script, and click on the displayed frame to obtain HSV values.

### 2. PixelConverter Class

The PixelConverter class provides functionality to capture pixel values from an OpenCV video feed and convert them into various formats such as BGR, RGB, Hex, HSV, and RGBA.

- **Usage:**
  - Import the `PixelConverter` class into your project.
  - Create an instance and run the `get_webcam_pixels` method to interactively capture pixel values.

- **Features:**
  - Conversion of pixel values into various formats.
  - Modular and object-oriented design for seamless integration.
  - Perfect for applications requiring color analysis and real-time interactive pixel insights.

- **Example:**
  ```python
  from pixel_converter import PixelConverter

  if __name__ == "__main__":
      pixel_converter = PixelConverter()
      pixel_converter.get_webcam_pixels()
  
## Upcoming Modules

1. Color Detection Modules (Upcoming)
Coming soon! Modules exploring color detection techniques for diverse applications.
Gain hands-on experience in detecting and analyzing colors in images and video feeds.

2. Color Masks and Filters (Upcoming)
Combine with upcoming color detection modules for advanced color manipulation.

## Author
Jacob Pitsenberger

## License
This software is licensed under the MIT License. By using this software, you agree to comply with the terms outlined in the license.