import pywhatkit
import os
from os import system

os.system("title Abhinav beats google.")
os.system("color 0a")
os.system("cls")
while True:
    search = input("What do you want to know more about? \n")
    print("Thinking....\n\n")
    os.system("color 07")
    pywhatkit.info(search)
    print("\n")
    input("Press Enter to continue...\n")
    os.system("color 0a")
    os.system("cls")