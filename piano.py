import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)


pyautogui.click(1026,379, duration= 2) #start no jogo

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(908,307, (0, 0, 0)):
        click(908,307)
    if pyautogui.pixelMatchesColor(979,298, (0, 0, 0)):
        click(979,298)
    if pyautogui.pixelMatchesColor(1049,303, (0, 0, 0)):
        click(1049,303)
    if pyautogui.pixelMatchesColor(1129,303, (0, 0, 0)):
        click(1129,303)
