import re

def invoke(phrase):
    return True if re.search(r'( ?(hey computer|boy|iron)|(computer|boy|iron))+', phrase) else False