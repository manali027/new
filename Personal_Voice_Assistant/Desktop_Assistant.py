import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import pyttsx3

import datetime
#from engine import Engine


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour()
    if(hour>=0 and hour<=12):
        speak("Hello,Good Morning")
        print("Hello ,Good Morning")
    elif(hour>12 and hour <=18):
        speak("Hello,Good afternoon")
        print("Hello,Good afternoon")
    else:
        speak("Hello,good evening")
        print("Hello,good evening")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio=r.listen(source)

        try:
           statement=r.recognize_google(audio,language='en-in')
           print(f"user said : {statement}\n")
        except Exception as e:
            speak("Pardon me,plaese repeat")
            return "None"
        return statement
    print("Loading your  assitant")
    speak("Loading your assistant")
    wishMe()



if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue







