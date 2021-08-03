import pyttsx3, random

GREETINGS_ARRAY = [
    'I\'m here',
    'I\'m hearing you',
    'I\'m listening to you sir',
    'What do you want?',
    'What do you want, leather?',
    'Am I your dog to listen to you every time?',
    'Well come on, ask me for something again',
    'Yes',
    'Yeah',
    'Yep',
    'Yea'
]

engine = pyttsx3.init()
voices = engine.getProperty('voices')     
engine.setProperty('voice', voices[2].id)

def invoke():
    engine.say(GREETINGS_ARRAY[random.randint(0, len(GREETINGS_ARRAY) - 1)])
    engine.runAndWait()
    pass