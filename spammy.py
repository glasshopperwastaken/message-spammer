import time
import pyautogui


time.sleep(2)
f = open("beemovie.txt", 'r')
for word in f:
    pyautogui.typewrite(word, 0.01)
    pyautogui.press('enter')
