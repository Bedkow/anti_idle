import ctypes
import time
import keyboard
import mouse
import os

#Path to a txt file to write in

os.startfile('C:/Users/xxxxxxxxx//Error.txt')

while True:
    time.sleep(20)  # delay by 20 seconds
    x_axis = 400
    y_axis = 400
    ctypes.windll.user32.SetCursorPos(x_axis, y_axis)
    while x_axis < 1200:
        x_axis = x_axis + 2
        ctypes.windll.user32.SetCursorPos(x_axis, y_axis)
        time.sleep(0.001)  # delay by 0.001 seconds
    while x_axis > 400:
        x_axis = x_axis - 2
        ctypes.windll.user32.SetCursorPos(x_axis, y_axis)
        time.sleep(0.001)  # delay by 0.001 seconds
    while y_axis < 600:
        y_axis = y_axis + 2
        ctypes.windll.user32.SetCursorPos(x_axis, y_axis)
        time.sleep(0.001)  # delay by 0.001 seconds
    while y_axis > 400:
        y_axis = y_axis - 2
        ctypes.windll.user32.SetCursorPos(x_axis, y_axis)
        time.sleep(0.001)  # delay by 0.001 seconds

    mouse.click(button='left')
    keyboard.send('Enter')
    keyboard.write('Error')