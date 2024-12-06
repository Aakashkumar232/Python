import pyautogui
import os
import time

os.system("spotify")
time.sleep(5)
pyautogui.hotkey('ctrl','l')
pyautogui.write('play song ',interval = 0.1)

for key in ['enter','pagedown','tab','enter','enter']:
    time.sleep(2)
pyautogui.press(key)

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('aakashk3741@gmail.com','57575353')
    server.sendmail('aakashk3741@gmail.com',to,content)
    server.close()

    
        elif 'email to Aakash' in query: 
            try:
               speak("what should i say?") 
               content = takecommand() 
               to = "aakashk3741@gmail.com"
               sendEmail(to.content)
               speak("Email has been sent!") 

           except Exception as e:
               print(e)
               speak("sorry my friend Aakash bro.i am not able to send this email")    




def openapps():
    speak("ok sir")

    if "microsoft edge" in query:
        sp.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

    elif 'pycharma'in query:
        sp.Popen("C:\Program Files\\JetBrains\\PyCharm Community Edition 2023.2.4\\bin\\pycharm64.exe") 

    elif 'microsoft word' in query: 
        word_path = r"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        sp.Popen(word_path)

    elif 'vs code' in query: 
        code_path = "C:\\Users\\Advance Laptop\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        sp.Popen(code_path)    

    elif 'spotify' in query:
        os.system("spotify")
        time.sleep(5)
        pyautogui.hotkey('ctrl','l')
        pyautogui.write('play song ',interval = 0.1)
        for key in ['enter','pagedown','tab','enter','enter']:
         time.sleep(2)
        pyautogui.press(key)


         elif 'vs code' in query:
           openapps()
     
       elif 'microsoft edge' in query: 
           openapps() 

       elif 'pycharm' in query:
           openapps()   

       elif 'microsoft word' in query:
           openapps()  

       elif 'spotify' in query:
           openapps() 

for i in range(3):
   a = input("Enter the password to open jarvish :- ")
   pw_file = open("password.txt","r")
   pw = pw_file.read()
   pw_file.close()
   if(a==pw):
      print("Welcome sir! ")
      break
   elif(i==2 and a!=pw):
      exit()
   elif(a!=pw):
      print("Please try again")     
             
 


