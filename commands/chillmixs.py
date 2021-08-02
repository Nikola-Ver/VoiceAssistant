import re, webbrowser

def invoke(phrase):
    print(phrase)
    if (re.search(r'chill mix', phrase)):
        webbrowser.open('https://www.youtube.com/watch?v=7NOSDKb0HlU', new=0, autoraise=True)
