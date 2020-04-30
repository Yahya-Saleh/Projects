import pyautogui as gui
from time import sleep

while True:
    p = gui.position()
    print(gui.position())
    sleep(1)
    