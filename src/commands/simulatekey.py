import re
from pynput.keyboard import KeyCode, Controller

PLAY_PAUSE_REG = r'^((pause)|(stop)|(play)|(continue))$'

def invoke(phrase):
    if (re.search(PLAY_PAUSE_REG, phrase)):
        keyboard = Controller()
        key = KeyCode.from_vk(0xB3)
        keyboard.press(key)
        keyboard.release(key)
