import re, sys, os, greetings

COMMANDS_DIR = './commands'
START_PHRASE = r'^( ?(hey (computer|boy|iron))|(computer|boy|iron) ?)+'


sys.path.insert(0, COMMANDS_DIR)
modules = [''.join(f.split('.')[:-1]) for f in os.listdir(COMMANDS_DIR) if os.path.isdir(f) == False]
for module in modules:
    exec(f'import {module}')


def recognize_command(phrase, is_phrase):
    if (is_phrase):
        for module in modules:
            exec(f'{module}.invoke("{phrase}")')
        return False
    else:
        without_start_phrase = re.sub(START_PHRASE, '', phrase)
        if (without_start_phrase != phrase and len(without_start_phrase) > 0):
            for module in modules:
                exec(f'{module}.invoke("{without_start_phrase}")')
            return False 
        elif(without_start_phrase != phrase):
            greetings.invoke()
            return True
        else:
            return False