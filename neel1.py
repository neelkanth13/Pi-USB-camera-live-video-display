import pyautogui
import os
import time


time.sleep(15)

###############################################################
# open Terminal window
###############################################################
pyautogui.PAUSE=1
pyautogui.click(x=142, y=19, clicks=1, interval=1, button='left')
################################################################
# Now, double left click on terminal tab so that i would auto
# adjuct PI 3.5 Touch Screen.
################################################################
pyautogui.PAUSE=1
pyautogui.click(x=200, y=161, clicks = 1, interval = 1, button='left')

pyautogui.PAUSE=1
pyautogui.click(x=137, y=1, clicks = 0, interval = 4)

pyautogui.PAUSE=1
pyautogui.click(x=137, y=10, clicks = 1, interval = 1, button='left')

pyautogui.PAUSE=1
pyautogui.click(x=137, y=10, clicks = 1, interval = 1, button='right')
pyautogui.PAUSE=1
pyautogui.click(x=267, y=169, clicks = 1, interval = 1, button='left')


pyautogui.PAUSE=1
pyautogui.click(x=267, y=169, clicks = 1, interval = 1, button='left')

os.system('sudo python3 uvcvideo_state_detect.py')
time.sleep(5)

pyautogui.PAUSE=1
pyautogui.click(x=352, y=18, clicks = 1, interval = 1, button='right')
pyautogui.PAUSE=1
pyautogui.click(x=330, y=159, clicks = 1, interval = 1, button='left')
time.sleep(1)
pyautogui.hotkey('alt', 'space')
time.sleep(1)
pyautogui.click(x=84, y=158, clicks = 1, interval = 1, button='left')


pyautogui.PAUSE=1
pyautogui.click(x=464, y=297, clicks = 1, interval = 1, button='left')
