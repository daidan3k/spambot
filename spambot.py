import pyautogui, time

import sys

from colorama import init

init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

pip install pyautogui

cprint(figlet_format("SpamBot", font="big"), "red", "on_grey", attrs=["bold"])


msj = input("Mensaje a enviar:")
numero = input("Numero de mensajes: ")
num = int(numero)

time.sleep(5)

for x in range(num):
    pyautogui.typewrite(msj)
    pyautogui.press("enter")


# for x in range(2):
# pyautogui.typewrite("./mensajes.txt")
# pyautogui.press("enter")
