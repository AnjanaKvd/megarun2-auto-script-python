from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con


def drag_left(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.SetCursorPos((x-86,y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def drag_right(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.SetCursorPos((x+86,y))
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

x = 280
y = 800
black = 100
y_stage = 450

middle_x = 280
left_x = 195
right_x = 366
delay = 0.6

while keyboard.is_pressed('q') == False:
    
      
    if pyautogui.pixel(middle_x, y_stage)[0] < black and pyautogui.pixel(middle_x, y_stage)[1] < black and pyautogui.pixel(middle_x, y_stage)[2] < black:
        drag_left(x, y)
        time.sleep(delay)
        drag_right(x, y)
    if pyautogui.pixel(left_x, y_stage)[0] < black and pyautogui.pixel(left_x, y_stage)[1] < black and pyautogui.pixel(left_x, y_stage)[2] < black:
        drag_right(x,y)
        time.sleep(delay)
        drag_left(x, y)
    if pyautogui.pixel(right_x, y_stage)[0] < black and pyautogui.pixel(right_x, y_stage)[1] < black and pyautogui.pixel(right_x, y_stage)[2] < black:
        drag_left(x,y)
        time.sleep(delay)
        drag_right(x, y)

