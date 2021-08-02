import re, os

SHUTDOWN_REG = r'shutdown'

def invoke(phrase):
    if (re.search(SHUTDOWN_REG, phrase)):
        os.system("shutdown -s -t 0")
       