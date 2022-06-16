
from tkinter import *
import speech_recognition as sr
import pyttsx3
from datetime import datetime

root=Tk()
root.geometry("500x500")

text_to_speech=pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
    

def r_audio():
    speak("how can I help you")
    speech_recognisor=sr.Recognizer()
    with sr.Microphone() as source:
        audio=speech_recognisor.listen(source)
        voice_date=""
        try:
            voice_data=speech_recognisor.recognize_google(audio,lang="en-in")
        except sr.UnknownValueError:
            print("please repeat i did not get that")
            speak("please repeat i did not get that")
    respond(voice_data)
    
def respond():
    voice_data=voice_data.lower()
    
            
    print(voice_data)
    if "name" in voice_data:
        speak("my name is thamannaa")
        print("my name is thamannaa")
    if "time" in voice_data:
        speak("current time is")
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
            

            
    
        

r_audio()
root.mainloop()

