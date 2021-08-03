import re, datetime, calendar, pyttsx3

TIME_NOW_REG = r'(what time is it now)|(^time$)'
HOURS_NOW_REG = r'(how many hours)|(^hours$)'
MINUTES_NOW_REG = r'(how many minutes)|(^minutes$)'
DATE_NOW_REG = r'(what date is it now)|(^date$)'
DAY_OF_WEEK_REG = r'(what )*day of( the)* week( now)*'

engine = pyttsx3.init()
voices = engine.getProperty('voices')     
engine.setProperty('voice', voices[2].id)

def invoke(phrase):
    if (re.search(TIME_NOW_REG, phrase)):
        engine.say(datetime.datetime.now().strftime("%H:%M:%S"))
        engine.runAndWait()

    if (re.search(HOURS_NOW_REG, phrase)):
        engine.say(datetime.datetime.now().strftime("%H hours"))
        engine.runAndWait()

    if (re.search(MINUTES_NOW_REG, phrase)):
        engine.say(datetime.datetime.now().strftime("%M minutes"))
        engine.runAndWait()
    
    if (re.search(DATE_NOW_REG, phrase)):
        engine.say(datetime.date.today().strftime("%B %d, %Y"))
        engine.runAndWait()

    if (re.search(DAY_OF_WEEK_REG, phrase)):
        day_of_week = calendar.day_name[datetime.date.today().weekday()]
        text = ''
        if (re.search(r'today', phrase)):
            text = f'today is {day_of_week}'
        elif(re.search(r'now', phrase)):
            text = f'now {day_of_week}'
        else:
            text = day_of_week 
        engine.say(text)
        engine.runAndWait()