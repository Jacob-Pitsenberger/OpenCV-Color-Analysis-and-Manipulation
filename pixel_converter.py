"""
Author: Jacob Pitsenberger
Date: 12/10/2023
"""

import cv2
import numpy as np


class PixelConverter:
    """
    PixelConverter class provides functionality to capture pixel values from an OpenCV video feed
    and convert them into various formats such as BGR, RGB, Hex, HSV, and RGBA.
    """

    def __init__(self, video_source=0):
        """
        Initialize the PixelConverter object with a video source.

        Parameters:
        - video_source (int): Index of the video source (default is 0 for the default webcam).
        """
        # Open a connection to the webcam
        self.cap = cv2.VideoCapture(video_source)

        # Initialize the current pixel and frame as None
        self.current_pixel = None
        self.frame = None

        # List to hold color space values for the current pixel
        self.current_pixel_info = []

    def on_mouse(self, event, x, y, flags, param):
        """
        Callback function for handling mouse events. Prints pixel values in various formats
        when the left mouse button is clicked.

        Parameters:
        - event (int): Type of mouse event.
        - x (int): X-coordinate of the mouse click.
        - y (int): Y-coordinate of the mouse click.
        - flags: Additional flags.
        - param: Additional parameters.

        Note: In the context of OpenCV or similar GUI libraries, these 'flags' and 'param' parameters
              are necessary because the GUI library calls the callback function and provides information
              about the mouse event. If you remove any of these parameters, the function signature becomes
              mismatched with what the GUI library expects, leading to a TypeError.
        """
        if event == cv2.EVENT_LBUTTONDOWN:
            # Get the BGR pixel value at the clicked location
            self.current_pixel = self.frame[y, x]

            # Convert BGR to other formats and store the pixel values in the list
            self.current_pixel_info = [
                self.current_pixel,  # The original pixel value in BGR format (default)
                tuple(reversed(self.current_pixel)),  # Convert BGR to RGB by reversing the order of the color channels
                "#{:02X}{:02X}{:02X}".format(*self.current_pixel),  # the color in hexadecimal format. The {:02X} format specifier ensures that each color channel is represented by two uppercase hexadecimal characters.
                cv2.cvtColor(np.uint8([[self.current_pixel]]), cv2.COLOR_BGR2HSV)[0][0],  # Convert BGR to HSV using cv2.cvtColor function
                tuple(self.current_pixel.tolist() + [255])  # Converts BGR to RGBA by appending an alpha value of 255 (fully opaque)
            ]

            # Print the pixel values in different formats in a single statement
            print(", ".join(f"{color_space}: {values}" for color_space, values in
                            zip(["BGR", "RGB", "Hex", "HSV", "RGBA"], self.current_pixel_info)))

    def get_webcam_pixels(self):
        """
        Run the PixelConverter application, capturing video feed and displaying it.
        """
        while True:
            # Capture frame-by-frame
            ret, self.frame = self.cap.read()

            # Display the frame
            cv2.imshow('frame', self.frame)

            # Set the callback function for mouse events
            cv2.setMouseCallback('frame', self.on_mouse)

            # Break the loop if 'q' key is pressed
            if cv2.waitKey(1) & 0XFF == ord('q'):
                break

        # Release the capture when everything is done
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    # Create an instance of PixelConverter and run the application
    pixel_converter = PixelConverter()
    pixel_converter.get_webcam_pixels()
