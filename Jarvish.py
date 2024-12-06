import pyttsx3
import speech_recognition as sr 
import datetime
from datetime import date
import wikipedia
import sys
import webbrowser
import pyautogui 
import pyaudio
from time import sleep
from pyautogui import sleep 
import os
import pyjokes    
import random 
import time
import subprocess as sp
import wolframalpha
# import face_recognition
# import numpy as np
# import cv2(for the camera)
# from main import taskExecution

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[0].id)  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# video = cv2.videocapture(0)
# face = face_recognition.load_image_file("C:\Users\Advance Laptop\Pictures\Camera Roll")
# faceencoding = face_recognition.face_encodings(face)[0]
# face_encoding_list = [faceencoding]
# face_encodings_list = []
# s = True
# face_coordinates = []

# while True:
#    speak('detecting for face')
#    _,frame = video.read()

#    resized_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
#    resized_frame_rgb = resized_frame[:,:,::-1]

#    if s:
#       face_coordinates = face_recognition.face_locations(resized_frame_rgb)
#       face_encodings = face_recognition.face_encodings(resized_frame_rgb,face_coordinates)

#       for faces in face_encodings:
#          matches = face_recognition.compare_faces(face_encodings_list,faces)
#          if matches[0] == True:
#             video.release()
#             speak('face matched')
#             cv2.destroyALLWindows()
#             TaskExicution()
#          else:
#             speak('face not matched') 
#             speak('try again')

#    cv2.imshow('face scan',frame)

#    if cv2.waitkey(1) & 0xFF == ord('q'):
#       break
             
# video.release()
# cv2.destroyALLWindows()



def lock():
   password = 57575353
   speak("please enter your password ")
   g = int(input("please enter your password :- "))
   if password==g:
      speak("your password matched successfully,welcome sir!")
   else:
      exit()   

def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("good morning sir!")

    elif hour>=12 and hour<18: 
        speak("good afternoon sir!")
    else:
        speak("good evening sir!")       
    
    speak("your most welcome in my world")
    speak("i am jarvish sir. please tell me how may i help you.")  

def tellday():
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1:'monday',2:'tuesday',3:'wednesday',4:'thursday',5:'friday',6:'saturday',7:'sunday'}      

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("the day is" + day_of_the_week)

def telldate():
          today = date.today()
          current_date = today.strftime("%D %M %Y")
          print("today's date is:-", current_date)
          speak("today's date is:- ")

def telltime():
           strTime = datetime.datetime.now().strftime("%H:%M:%S")             
           speak(f"sir, the time is {strTime}")
           print("the time is:-",strTime)                 
   
def takecommand():                          #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")  
        r.pause_threshold = 1
        audio = r.listen(source)

    try:  
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n") 

    except Exception as e:                     # print(e)
        print("say that again please...")
        return "None"      
    return query

if __name__ == "__main__":
   speak("your device is password protected, kindaly provide the required password")
   lock()
   wishMe()
   tellday()
   telldate()
   telltime()

   while True:
#    if 1:
       query = takecommand().lower()

       if 'wikipedia' in query:
           speak("ok sir!")
           speak('searching wikipedia...') 
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query,sentences = 2)
           speak("according to wikipedia")
           print(results)
           speak(results)

       elif "change password" in query:
          speak("ok sir!")
          speak("what's the new password")
          new_pw = input("Enter the new password:- ")
          new_password = open("password.txt","w")
          new_password.close()
          speak("Done sir")
          speak(f"your new password is{new_pw}")
          
       elif 'open my google' in query: 
           speak("ok sir!")
           webbrowser.open("www.google.com")

       elif 'open my whatsapp' in query:
         speak("ok sir!")
         webbrowser.open("www.whatsapp.com") 

       elif 'open my facebook' in query:
           speak("ok sir!")
           webbrowser.open("www.facebook.com")    

       elif 'open my stackoverflow'in query:
           speak("ok sir!") 
           webbrowser.open("www.stackoverflow.com") 

       elif 'open my reddit' in query:
          speak("ok sir!")
          webbrowser.open("www.reddit.com")    

       elif " open my microsoft edge" in query:
        speak("ok sir!")
        sp.Popen("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

       elif 'open my pycharm'in query:
        speak("ok sir!")
        sp.Popen("C:\Program Files\\JetBrains\\PyCharm Community Edition 2023.2.4\\bin\\pycharm64.exe") 

       elif 'open my microsoft word' in query: 
        speak("ok sir!")
        word_path = r"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        sp.Popen(word_path)

       elif 'open my vs code' in query: 
        speak("ok sir!")
        code_path = "C:\\Users\\Advance Laptop\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path) 

       elif 'open my notepad' in query:
          speak("ok sir!")
          apath = "C:\\Users\\Advance Laptop\\Desktop\\Notepad - Shortcut.lnk"    
          os.startfile(apath)

       elif 'open my cmd' in query:
          speak("ok sir!")
          os.system("start cmd")

       elif 'play music' in query:
          speak("ok sir!")
          music_dir = "C:\\Users\\Advance Laptop\\Music"   
          songs = os.listdir(music_dir)
          rd = random.choice(songs)
          os.startfile(os.path.join(music_dir,rd))

       elif 'open my spotify' in query:
        speak("ok sir!")
        os.system("spotify")
        time.sleep(5)
        pyautogui.hotkey('ctrl','l')
        pyautogui.write('play song ',interval = 0.1)
        for key in ['enter','pagedown','tab','enter','enter']:
         time.sleep(2)
        pyautogui.press(key) 

       elif 'open my new tab' in query:
          speak("ok sir!")
          pyautogui.hotkey('ctrl','t') 
          speak("here is your new tab")
          
       elif 'minimise the window' in query:
          speak("ok sir!")
          pyautogui.hotkey('win','d') 
          speak("window minimise successfully")  

       elif 'volume up' in query:
          speak("ok sir!")
          pyautogui.hotkey('volumeup')
          speak("volume up successfully")

       elif 'volume down' in query:
          speak("ok sir!")
          pyautogui.hotkey('volumedown')
          speak("volume down successfully")

       elif 'volume mute' in query:
          speak("ok sir!")
          pyautogui.hotkey('volumemute')
          speak("volume mute successfully")

       elif 'open my favourite music on youtube' in query:
          speak("ok sir!")
          webbrowser.open("https://youtu.be/SJuqqsX8aEc?si=HhMNP0mGgxDkYUh-") 

       elif 'open my youtube channel' in query:
          speak("ok sir!")
          webbrowser.open("https://www.youtube.com/@kaartik123m") 

       elif 'open my youtube' in query: 
           speak("ok sir!")
           webbrowser.open("www.youtube.com")

       elif 'open my instagram' in query:
          speak("ok sir!")
          webbrowser.open("www.instagram.com")

       elif 'calculate the number' in query:
          speak("ok sir!")
          app = wolframalpha.Client("G6KL6L-5GKTEPKQHJ")
          speak("what should i calculate, sir!")
          query = input("enter the query:")
          res = app.query(query)
          speak(next(res.results).text)
          print(next(res.results).text)


       elif 'open my bluetooth' in query:
          speak("ok sir!")
          sleep(1)
          pyautogui.click(x=1651, y=1047)
          sleep(1)
          pyautogui.click(x=1676, y=188)
          sleep(1)
          pyautogui.click(x=1848, y=144)

       elif 'open my wi-fi' in query:
          speak("ok sir!")
          sleep(1)
          pyautogui.click(x=1652, y=1041)
          sleep(1)
          pyautogui.click(x=1516, y=182)
          sleep(1)
          pyautogui.click(x=1778, y=156)
          sleep(1)
          pyautogui.click(x=1846, y=143)

      
     #  elif 'open my google' in query:
      #     speak("sir! what i should search on google")
      #     query = takecommand().lower()
      #     webbrowser.open(f"{query}") 

      #  elif 'whatsapp' in query:
      #     sleep(1)
      #     pyautogui.click(x=995, y=1050)
      #     sleep(1)
      #     pyautogui.click(x=394, y=218)
      #     sleep(1)
      #     pyautogui.click(x=1068, y=173)

      #  elif 'restart the system' in query:
      #     os.system("shutdown/r/t 0")

      #  elif 'shutdown the system' in query:
      #     os.system("shutdown/s/t 0")

       elif 'open' in query:
          speak("ok sir!")
          query = query.replace("open","")
          query = query.replace("jarvish","")
          pyautogui.press("super")
          pyautogui.typewrite(query)
          pyautogui.sleep(2)
          pyautogui.press("enter")

       elif 'tell me a joke' in query:
          speak("ok sir!")
          joke = pyjokes.get_joke()
          speak(joke)
          print(joke)

       elif 'hi' in query:
          speak("hi sir, how are you? ") 
          print("hi sir, how are you?")

       elif 'i am fine' in query:
          speak("thank you ")
          print("thank you ")

       elif 'and you' in query:
          speak("i am also fine ") 
          print("i am also fine ")  

       elif 'who made you' in query:
          speak("i have created to me my god kaartik patel  ")   
          print("i created to me my god kaartik patel ")     

       elif 'good bye' in query:
          speak("ok sir!")
          speak("thanks for using me sir,you can call me any time,have a nice day")   
          sys.exit()
  
       



