import pyautogui
import cv2

top_region = pyautogui.screenshot(region=(250, 400, 450, 152))

left_lane = [i for i in range(250, 407)]
mid_lane = [i for i in range(407, 542)]
right_lane = [i for i in range(542, 700)]

middle_x_line = 225

top_region = [250, 400, 450, 152]
bottom_region = [250, 775, 450, 152]
man_region = [250, 777, 450, 80]

manX, manY = pyautogui.locateCenterOnScreen('man.png', region=(250, 777, 450, 80), confidence=0.8, grayscale=True)
print(left_lane)