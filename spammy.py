import time
import pyautogui

#The main script, make adjustments if you'd like.

time.sleep(2)
print("Spamming has begun, so prepare for epic trolling ehehe")
f = open("beemovie.txt", 'r')
for word in f:
    pyautogui.typewrite(word, 0.09)
    pyautogui.press('enter')
    time.sleep(0.5)
