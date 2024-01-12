"""
Pixel Value Capture Script

This script opens a connection to the default webcam, captures the video feed,
and allows the user to click on the displayed frame to obtain the HSV value of
the pixel at the clicked location. The script continuously displays the video
feed, prints the HSV value in the console when the left mouse button is clicked, and appends these values to a list.
After exiting from the video loop by pressing the 'q' key, the upper and lower bounds for that range of hsv pixels
values are printed to the console for binary masking use.

Author: Jacob Pitsenberger
Date: 12/10/2023
updated: 1/11/2024
"""

import cv2
import numpy as np

# Create a list variable to store the hsv_pixel value range
vals = []

def on_mouse(event, x, y, flags, param):
    # Check if the event was the left mouse button being clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the BGR pixel value at the clicked location
        pixel = frame[y, x]

        # Convert BGR to HSV and print the pixel value
        hsv_pixel = cv2.cvtColor(np.uint8([[pixel]]), cv2.COLOR_BGR2HSV)
        print("HSV:", hsv_pixel[0][0])
        # Append the pixel value to the values list
        vals.append(hsv_pixel[0][0])

def get_thresh_from_vals(vals: np.array) -> np.array:
    # Calculate the minimum and maximum values for each channel
    min_h, min_s, min_v = np.min(vals, axis=0)
    max_h, max_s, max_v = np.max(vals, axis=0)
    lower_color = [min_h, min_s, min_v]
    upper_color = [max_h, max_s, max_v]
    # Output the results
    print(f"lower bound: {lower_color}")
    print(f"upper bound: {upper_color}")
    return lower_color, upper_color


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
low, up = get_thresh_from_vals(vals)

