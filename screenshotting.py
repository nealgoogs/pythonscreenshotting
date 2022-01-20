import pyautogui
from win32api import GetKeyState
from win32con import VK_CAPITAL
 
i = 0
 
 
while True:
    if GetKeyState(VK_CAPITAL) == 1:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:\AI TRAINING\Screenshots' + str(i) + '.png')
        myScreenshot.close()
 
        i += 1