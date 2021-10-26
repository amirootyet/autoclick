import pyautogui
from time import sleep

print("[i] Running autoclick. Press ctrl+c to exit...")
while True:
    buttonLocation = pyautogui.locateOnScreen('manual.png', confidence = 0.7)
    if buttonLocation:
        buttonPoint = pyautogui.center(buttonLocation)
        buttonX, buttonY = buttonPoint
        pyautogui.click(buttonX, buttonY)
        print("[+] Found and clicked.")

    sleep(5)

