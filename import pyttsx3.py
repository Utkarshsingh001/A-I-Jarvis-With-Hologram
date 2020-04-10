import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pymedtermino


print("Initialising Meidosa.....")


master="sir"
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def Hindi():
    speak("namastey")
    speak("me apki kaise help kar sakti hu ?")


    
def English():
    speak("Hi")
    speak("How can i help you ?")
     


    

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour >=0 and hour<=12:
        speak("Good Morning" + master)
    elif hour>=12 and hour<=18:
        speak("Good AfterNoon " + master)
    else:
        speak("Good Night" + master)

def takecmd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try :
        print("Recognising...")
        query = r.recognize_google(audio , language='en-in')
        print("\n" + query)
    except Exception as e:
        speak("Say that again please")
        query=None
    return query

speak("Initialising Miedosa" )
wishMe()
#logic for chat bot
speak("Would You like to continue in English or alter to Hindi ?")
query=takecmd()
if "hindi" in query.lower():
    Hindi()
else:
    English()
