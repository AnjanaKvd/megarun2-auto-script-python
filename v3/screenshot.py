import pyautogui

# iml = pyautogui.screenshot(region=(250, 775, 450, 152)) # bottom
# iml = pyautogui.screenshot(region=(250, 777, 450, 80)) #man
for i in range(0, 1000):
    iml = pyautogui.screenshot(region=(55, 400, 330, 50)) #top
    iml.save(f"images/top-test{i}.png")