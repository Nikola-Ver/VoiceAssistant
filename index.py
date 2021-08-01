import pyaudio,os
import speech_recognition as sr
import commands

r = sr.Recognizer()

with sr.Microphone() as source:
    while True:
        try:
            audio = r.listen(source)
            phrase = r.recognize_google(audio)
            commands.recognize_command(phrase)
        except: 
            pass