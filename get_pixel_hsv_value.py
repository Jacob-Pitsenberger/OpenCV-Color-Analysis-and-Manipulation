"""
Pixel Value Capture Script

This script opens a connection to the default webcam, captures the video feed,
and allows the user to click on the displayed frame to obtain the HSV value of
the pixel at the clicked location. The script continuously displays the video
feed and prints the HSV value in the console when the left mouse button is clicked.

Author: Jacob Pitsenberger
Date: 12/10/2023
"""

import cv2
import numpy as np

def on_mouse(event, x, y, flags, param):
    """
    Callback function for handling mouse events. Prints the HSV value of the pixel
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
    # Check if the event was the left mouse button being clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the BGR pixel value at the clicked location
        pixel = frame[y, x]

        # Convert BGR to HSV and print the pixel value
        hsv_pixel = cv2.cvtColor(np.uint8([[pixel]]), cv2.COLOR_BGR2HSV)
        print("HSV:", hsv_pixel[0][0])


# Open a connection to the webcam (you may need to change the index)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('frame', frame)

    # Set the callback function for mouse events
    cv2.setMouseCallback('frame', on_mouse)  # Make sure 'Frame' matches the window name in cv2.imshow

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

# Release the capture when everything is done
cap.release()
cv2.destroyAllWindows()
