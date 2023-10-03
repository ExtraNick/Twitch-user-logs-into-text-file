import webbrowser
import pyautogui
import time
import os

name = os.path.basename(__file__)
name = (os.path.splitext(name)[0])

#Replace the {ChannelNameHere} below with the channel name whose logs you wanna see
url = "https://www.twitch.tv/popout/{ChannelNameHere}/viewercard/" + name

webbrowser.open(url, new=0, autoraise=True)
time.sleep(3)

pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
pyautogui.press('win')
pyautogui.write('note')
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('ctrl','s')
pyautogui.write('Chat log user ' + name)
pyautogui.press('enter')
pyautogui.hotkey('ctrl','o')
time.sleep(1)
pyautogui.hotkey('ctrl','f')
pyautogui.write('Chat log user ' + name)
time.sleep(1)
pyautogui.press('down')
pyautogui.press('down')
pyautogui.hotkey('ctrl','c')