import pyttsx3
import os
from os import system

talkback = pyttsx3.init()
voices = talkback.getProperty('voices') 
talkback.setProperty('voice', voices[1].id)

os.system("color 0a")
os.system("cls")
while True:
    ask = input("Would you like to save this file as an mp4?\n")
    robot = input("What do you want me to say?\n")
    talkback.say(robot)
    if ask == "yes" or "ye" or "ya" or "ok" or "y" or "yea":
        print("Exporting Your Text As Speech")
        talkback.save_to_file(robot, 'export.mp3')
    talkback.runAndWait()
    os.system("cls")
