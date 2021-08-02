import re, datetime, pyttsx3

TIME_NOW_REG = r'(what time is it now)|(time)'
DATE_NOW_REG = r'(what date is it now)|(date)'

engine = pyttsx3.init()
voices = engine.getProperty('voices')     
engine.setProperty('voice', voices[2].id)

def invoke(phrase):
    if (re.search(TIME_NOW_REG, phrase)):
        engine.say(datetime.datetime.now().strftime("%H:%M:%S"))
        engine.runAndWait()
    
    if (re.search(DATE_NOW_REG, phrase)):
        engine.say(datetime.date.today().strftime("%B %d, %Y"))
        engine.runAndWait()