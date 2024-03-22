import pywhatkit
import os
from os import system
os.system("title  Beats Spotify.")
os.system("color 0a")
os.system("cls")
while True:
	song=input("Which song would you like to hear?\n")
	print('Processing your information.')
	pywhatkit.playonyt(song)
	os.system("cls")
