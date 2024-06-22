from pynput import keyboard
import time

def on_press(key):
  try:
    print('alphanumeric key {0} pressed'.format(key.char))
    keyboard.press(key.char)
  except AttributeError:
    print('special key {0}'.format(key))

def on_release(key):
  try:
    print('{0} released'.format(key.char))
    # if key == keyboard.Key.esc:
    #   print('yup')
    #   return False
  except AttributeError:
    print('special key {0}'.format(key))

with keyboard.Listener(on_press=on_press, on_release=on_release, suppress=True) as listener:
  listener.join()
