from time import sleep

import pyautogui

while True:
    sleep(.2)
    pyautogui.click('img/trash.png')
    sleep(.4)
    pyautogui.click('img/yes.png')
    sleep(.2)