import sys, os, start_communicate

COMMANDS_DIR = './commands'

sys.path.insert(0, COMMANDS_DIR)
modules = [''.join(f.split('.')[:-1]) for f in os.listdir(COMMANDS_DIR) if os.path.isdir(f) == False]
for module in modules:
    exec(f'import {module}')


def recognize_command(phrase, is_phrase):
    if (is_phrase):
        for module in modules:
            exec(f'{module}.invoke({phrase})')
        return False
    else:
        return start_communicate.invoke(phrase)