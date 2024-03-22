import sys
import random
import os
import time
import pygame as musicpp
musicpp.mixer.init()
musicpp.mixer.music.load('bis.wav')
musicpp.mixer.music.play(999)
os.system("cls")
os.system("color 0a")
os.system("title Huge Baller 8-Ball")
print("Checking For Internet: CONNECTED")
time.sleep(1)
os.system("color 0f")
print(f'''
 ╔──────────────────────────────────────────────╗
 |           Author: Abhinav Ranish             |
 |       Magic 8-Ball v1.1 - AbhiQ Networks     |
 |       Follow Me On - Github & Instagram      |
 |           Github - abhinav-ranish            |
 |            Made with 💖 & Python             |
 ┖──────────────────────────────────────────────┙
 ''')
time.sleep(5)
try:
    try:
    
        while True : 
            os.system("cls")
            os.system("color 0e")
            ball = input("Ask the magic 8 ball a question: \n")
            reply = random.randint(1,8)   
            print("") 
            if reply == 1:
                os.system("color 0b")
                print("Holy Shit! My Answer is a No.\n")
                time.sleep(5)
            elif reply == 2:
                os.system("color 0b")
                print("My Heart Says Yes But My Mind Says No. \nAsk Again Later.\n")
                time.sleep(5)
            elif reply == 3:
                os.system("color 0b")
                print("I was distracted by my huge brain. \nAsk Again in Sometime.\n")
                time.sleep(5)
            elif reply == 4:
                os.system("color 0b")
                print("Wait do you see a moron. Yes its looking right at me. \nThe Answer is Yes\n")
                time.sleep(5)
            elif reply == 5:
                os.system("color 0b")
                print("I am in a deep conversation with alexa. \nTalk to me later\n")
                time.sleep(5)
            elif reply == 6:
                os.system("color 0b")
                print("I asked Google and Google Said Yes. \nMy Answer is Yes\n")
                time.sleep(5)
            elif reply == 7:
                os.system("color 0b")
                print("Whats in your head? Filled with soil I guess. \nMy Answer is No.\n")
                time.sleep(5)
            elif reply == 8:
                os.system("color 0b")
                print("If You wanna do it go for it. My Answer is the opposite of your answer.\n")
                time.sleep(5)
    except KeyboardInterrupt:
        os.system("cls")
        os.system("color 0f")
        ezclap = input("Thank you for playing with Magic 8Ball.\n")
        sys.exit()
except KeyboardInterrupt:
    ezclap = input("Noob Just Press Enter To Exit")
    