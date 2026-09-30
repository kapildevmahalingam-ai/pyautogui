import pyautogui
import time
from datetime import datetime

pyautogui.failSafe = True
pyautogui.PAUSE = 1.0

print("Step 1: to launch the chrome browser")
pyautogui.hotkey("win", "r")
time.sleep(1)

pyautogui.write("chrome --incognito")
pyautogui.press("enter")
time.sleep(3)

print("Step 2: Go to the website")
pyautogui.hotkey("ctrl", "t")
time.sleep(1)
pyautogui.typewrite('https://www.accuweather.com/en/in/chennai/206671/10-day-weather-forecast/206671', interval=0.1)
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(484.5,40)
time.sleep(1)

print("Step 3: Copy the all the text from the website")
pyautogui.hotkey("ctrl", "a")
time.sleep(1)
pyautogui.hotkey("ctrl", "c")

print("Step 4: Open Notepad and paste the copied text")
pyautogui.hotkey("win", "r")
time.sleep(1)
pyautogui.write("notepad")
pyautogui.press("enter")
time.sleep(2)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.hotkey("ctrl", "s")
time.sleep(1)
pyautogui.write("weather_forecast3.txt")
pyautogui.press("enter")
time.sleep(5)

print("Step 5: close the notepad and chrome browser")
pyautogui.hotkey("alt", "f4")
time.sleep(5)
pyautogui.hotkey("alt", "f4")
time.sleep(5)

print("Step 6: successfully completed the task")