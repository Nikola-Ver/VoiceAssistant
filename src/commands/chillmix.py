import re, webbrowser

CHILL_MIX_REG = r'chill mix'

def invoke(phrase):
    if (re.search(CHILL_MIX_REG, phrase)):
        webbrowser.open(
            'https://www.youtube.com/embed/7NOSDKb0HlU?&autoplay=1;frameborder=0', 
            new = 0, 
            autoraise = True
        )