import pyautogui
from time import sleep
from pynput import keyboard
from argparse import ArgumentParser

keys_pressed = set()

def on_key_release(key):
    try:
        keys_pressed.remove(key.char)
    except AttributeError:
        pass

def on_key_press(key):
    try:
        keys_pressed.add(key.char)
    except AttributeError:
        pass

def main():
    # Parse key to press
    parser = ArgumentParser()
    parser.add_argument('-k', '--key', help='Key to press down')
    args = parser.parse_args()

    # Set up listener for key presses and releases
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        sleep(5)
        while True:
            # Check for the key combination 'J' + 'K'
            if 'j' in keys_pressed and 'k' in keys_pressed:
                break

            pyautogui.keyDown(args.key if args.key else 'w')

if __name__ == '__main__':
    main()
