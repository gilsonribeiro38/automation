import pyautogui
import time
image = pyautogui.locateAllOnScreen(r'C:\\images\\target_image.png')
while str(image) == "None":
    time.sleep(1)
    if str(image) != "None":
        pyautogui.alert("Found image")
        break
    else:
        image = pyautogui.locateAllOnScreen(r'C:\\images\\target_image.png')
print("END")


