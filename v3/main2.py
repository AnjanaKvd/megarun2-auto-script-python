from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

def drag_left(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.SetCursorPos((x - 86, y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def drag_right(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.SetCursorPos((x + 86, y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

x = 475
y = 800
black = 100
y_stage = 400

middle_x = 475
left_x = 389
right_x = 561

# Initialize the position to the middle
current_x = middle_x

while keyboard.is_pressed('q') == False:
    # Check the pixels at the current position and adjust the character's position
    if pyautogui.pixel(current_x, y_stage)[0] < black and pyautogui.pixel(current_x, y_stage)[1] < black and pyautogui.pixel(current_x, y_stage)[2] < black:
        if current_x == middle_x:
            # If in the middle, move to the left
            drag_left(x, y)
            current_x = left_x
        elif current_x == left_x:
            # If on the left, move to the right
            drag_right(x, y)
            current_x = right_x

    # Sleep to control the loop speed
    time.sleep(0.1)
