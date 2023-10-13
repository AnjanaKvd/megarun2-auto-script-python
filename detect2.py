import cv2
import numpy as np
import subprocess
from io import BytesIO
from PIL import Image

# Function to capture the screen
def capture_screen():
    # Capture the screen and return it as a NumPy array
    process = subprocess.Popen("adb exec-out screencap -p", shell=True, stdout=subprocess.PIPE)
    image_data = process.stdout.read()
    image = Image.open(BytesIO(image_data)).convert('RGB')
    return np.array(image)

# Function to check if the pixel color at a specific coordinate matches the expected color
def check_pixel_color(screen, x, y, expected_color):
    pixel_color = screen[y, x]  # Get the color of the pixel at (x, y)
    print(pixel_color)
    # Compare the pixel color to the expected color (in BGR format)
    if np.array_equal(pixel_color, expected_color):
        print("Obstacle Detected!")

# Define the coordinate (x, y) of the pixel to check
pixel_x = 360  # Adjust as needed
pixel_y = 870  # Adjust as needed

# Define the expected color of the obstacle (in BGR format)
expected_color = np.array([70, 62, 60])  # Black color

while True:
    screen = capture_screen()
    check_pixel_color(screen, pixel_x, pixel_y, expected_color)
