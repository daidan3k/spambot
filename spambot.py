from pyfiglet import figlet_format
from termcolor import cprint
import pyautogui
import time
import os
import sys

from colorama import Fore, Back, Style, init

# Functions


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected

cprint(figlet_format("SpamBot", font="big"),
       "red", "on_grey", attrs=["bold"])


msj = input(Fore.RED + Style.BRIGHT + "Mensaje a enviar: " +
            Fore.WHITE + Style.RESET_ALL)
numero = input(Fore.RED + Style.BRIGHT +
               "Numero de mensajes: " + Fore.WHITE + Style.RESET_ALL)
tiempo = input(Fore.RED + Style.BRIGHT + 'Tiempo entre mensajes (s):' + Fore.WHITE + Style.RESET_ALL)

num = int(numero)

clear()

cuenta_atras = 11
for i in range(1, cuenta_atras+1):
    print(Fore.MAGENTA + Style.BRIGHT +
          "Entre en el campo de insercion de texto y espere unos segundos...")
    print("     ", cuenta_atras-i)
    time.sleep(1)
    clear()

print(Fore.MAGENTA + Style.BRIGHT +
      "Iniciando Spam...")

mensajes_enviados = 1
for x in range(num):
    pyautogui.typewrite(msj)
    time.sleep(tiempo)
    pyautogui.press("enter")
    print(mensajes_enviados, "mensajes enviados")
    mensajes_enviados = mensajes_enviados+1

print(Fore.MAGENTA + Style.BRIGHT +
      "Spam Finalizado")

print(Fore.BLUE + Style.BRIGHT +
      "Pulsa 'intro' para cerrar el programa")

input()