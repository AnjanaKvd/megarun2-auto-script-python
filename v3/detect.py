from pyautogui import * 
import pyautogui 
import time 
import numpy as np
import cv2

template = cv2.imread("rock2.png", cv2.IMREAD_GRAYSCALE)
# cv2.imshow("template", template)
# cv2.waitKey()
# cv2.destroyAllWindows()
while True:
    top_region = pyautogui.screenshot(region=(55, 400, 330, 100))
    top_region = np.array(top_region)
    top_region = cv2.cvtColor(top_region, cv2.COLOR_BGR2GRAY)

    height = top_region.shape[0]
    width = top_region.shape[1]

    template = np.uint8(template)
    top_region = np.uint8(top_region)
    
    result = cv2.matchTemplate(top_region, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.91:
        if(max_loc[0] in range(55, 165)):
           print("left lane")
        elif(max_loc[0] in range(175, width)):
            print("right lane")
        else:
            print("mid lane")