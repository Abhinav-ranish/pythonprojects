import webbrowser,sys,os,time
os.system("cls")
os.system("color 0a")
os.system("title Youtube to Mp3/Mp4")
print("Checking For Internet: CONNECTED")
time.sleep(1)
os.system("color 0f")
print(f'''
 ╔──────────────────────────────────────────────╗
 |           Author: Abhinav Ranish             |
 |       Youtube2Mp3  v1.1 - AbhiQ Networks     |
 |       Follow Me On - Github & Instagram      |
 |           Github - abhinav-ranish            |
 |            Made with 💖 & Python             |
 |     Api Credits - youtubetomp3converterapi   |
 ┖──────────────────────────────────────────────┙
 ''')
try:
    while True : 
        yturl = input("Enter ID of youtube video. https://youtube.com/watch?v=_____ \n")
        format = input("\nEnter 1 for Mp3 \n\nEnter 2 for Mp4 \n\n")
        if format == "2":
            link1 = "https://api.download-lagu-mp3.com/@api/button/videos/" + yturl
            webbrowser.open_new_tab(link1)
        elif format == "1":
            link2 = "https://api.download-lagu-mp3.com/@api/button/mp3/"+ yturl
            print(link2)
            webbrowser.open_new_tab(link2)
        elif format =="":
            print("Sorry. Incorrect information provided.")
except KeyboardInterrupt:
        os.system("cls")
        os.system("color 0f")
        ezclap = input("Thank you for using Youtube2Mp3.\n")
        sys.exit()


