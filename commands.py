import re, sys, os

sys.path.insert(0, './commands')
modules = os.listdir('./')
for module in modules:
    exec(f'import {module}')

def recognize_command(phrase):
    print(phrase)
    if(re.search(r'(hey computer|boy|iron)|(computer|boy|iron)', phrase)):
        print('da')
    else:
        print('no')