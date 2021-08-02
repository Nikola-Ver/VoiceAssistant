import pyaudio,os
import speech_recognition as sr
import commands

r = sr.Recognizer()

with sr.Microphone() as source:
    is_listening_command = False
    while True:
        try:
            audio = r.listen(source)
            phrase = r.recognize_google(audio)
            is_listening_command = commands.recognize_command(phrase, is_listening_command)
        except: 
            pass