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

# Function to detect obstacles
def detect_obstacles(screen, obstacle_template):
    # Convert both images to grayscale (single-channel)
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    obstacle_template_gray = cv2.cvtColor(obstacle_template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(screen_gray, obstacle_template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    threshold = 0.6
    print(max_val)
    if max_val > threshold:
        print("Obstacle Detected!")

# Load the obstacle template
obstacle_template = cv2.imread("obstacle1.png")

while True:
    screen = capture_screen()
    detect_obstacles(screen, obstacle_template)
