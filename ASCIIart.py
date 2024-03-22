import pywhatkit
import os
from os import system
os.system("title Abhinav Makes Images Smesky.")
os.system("color 0a")
os.system("cls")
location_input = input("Where is the Image Located? \n Please Make sure your format is correct. (C:/Users/.../image.png) \n")
location_output = input("Where do you want to store the smesky image text file? \n Please Make sure your format is correct. (C:/Users/.../image.png) \n ")
print("Processing! Making Your Picture As Accurate As Possible.")
print("Visit abhinavranish.gq for more smecksy stuff. :)")
pywhatkit.image_to_ascii_art(location_input,location_output)

input("Press Enter to quit...")
os.system("cls")
