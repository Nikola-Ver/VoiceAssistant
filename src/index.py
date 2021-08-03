import pyaudio,os
import speech_recognition as sr
import commands

r = sr.Recognizer()

with sr.Microphone() as source:
    is_listening_command = False
    while True:
        try:
            r.adjust_for_ambient_noise(source)
            r.energy_threshold = 300 
            audio = r.listen(source, phrase_time_limit=7)
            phrase = r.recognize_google(audio)
            is_listening_command = commands.recognize_command(phrase, is_listening_command)
        except: 
            pass