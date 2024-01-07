"""
Author: Jacob Pitsenberger
Date: 1/7/2024

This module provide a powerful tool for real-time color detection of object specific colors through masking.

Reference for understanding how masks are found for specific colors via thresholding:
https://docs.opencv.org/3.4/df/d9d/tutorial_py_colorspaces.html

"""
import cv2
import numpy as np

class ColorDetector:
    """
    ColorDetector class provides functionality to apply a color mask to an OpenCV video feed
    using pre-defined HSV-value ranges for masking specific colors.

    Attributes:
    - COLOR_RANGES (dict): Dictionary mapping color names to their respective HSV ranges.

    Methods:
    - __init__(self, video_source=0): Initializes the ColorDetector object with a video source.
    - create_color_mask(self, color): Creates a color mask for the specified color based on HSV range.
    - run(self): Runs the ColorDetector application, capturing video feed, applying a color mask, and displaying it.
    """

    # Define HSV color ranges for different colors (obtained by getting hsv values for specific objects).
    COLOR_RANGES = {
        'red': ([160, 40, 200], [180, 120, 255]),
        'green': ([50, 40, 50], [90, 255, 255]),
        'blue': ([90, 50, 50], [120, 255, 255]),
        'yellow': ([20, 100, 100], [30, 255, 255]),
        'purple': ([125, 50, 50], [140, 255, 255]),
        # Add more colors as needed
    }

    def __init__(self, video_source=0):
        """
        Initialize the ColorDetector object with a video source.

        Parameters:
        - video_source (int): Index of the video source (default is 0 for the default webcam).
        """
        # Open a connection to the webcam and initialize the current frame to None
        self.frame = None
        self.cap = cv2.VideoCapture(video_source)

    def create_color_mask(self, color):
        """
        Create a color mask for the specified color based on HSV range.

        Parameters:
        - color (str): Name of the color ('red', 'green', etc.).

        Returns:
        - result (numpy.ndarray): Frame with the color mask applied.
        """
        try:
            # Convert the frame to HSV
            hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

            # Check if the specified color is in the predefined color ranges
            if color in self.COLOR_RANGES:
                # Get the HSV range for the specified color
                lower_color, upper_color = self.COLOR_RANGES[color]
            else:
                raise ValueError("Unsupported color. Choose from: " + ', '.join(self.COLOR_RANGES.keys()))

            # Create a mask based on the specified HSV range
            color_mask = cv2.inRange(hsv, np.array(lower_color), np.array(upper_color))

            # Apply the mask to the original frame
            result = cv2.bitwise_and(self.frame, self.frame, mask=color_mask)

            return result

        except Exception as e:
            print(f"Error creating color mask: {e}")
            return None

    def run(self):
        """
        Run the ColorDetector application, capturing video feed, applying a color mask, and displaying it.
        """
        try:
            print(f'Color Choices: {color_detector.COLOR_RANGES.keys()}')
            color = input("Specify Color Mask: ")
            print(f'Applying {color} color mask to video feed...')
            while True:
                # Capture frame-by-frame
                ret, self.frame = self.cap.read()

                # Apply color mask to the frame (change the color here if needed)
                frame = self.create_color_mask(color)

                # Display the frame
                cv2.imshow('frame', frame)
                # change waitKey for VGA: 25 fps ~= waitKey(40)
                key: int = cv2.waitKey(40)

                if key == ord('q'):
                    break
                elif key == ord('c'):
                    print(f'Color Choices: {color_detector.COLOR_RANGES.keys()}')
                    color = input("Specify Color Mask: ")
                    print(f'Applying {color} color mask to video feed...')

            # Release the capture when everything is done
            self.cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            print(f"Error running Color Detector application: {e}")


if __name__ == "__main__":
    # Create an instance of ColorDetector and run the application
    color_detector = ColorDetector()
    color_detector.run()
