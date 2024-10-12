import os

def text_to_speech(text):
    command = f'espeak "{text}"'
    os.system(command)
