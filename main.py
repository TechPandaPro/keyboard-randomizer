from pynput.keyboard import Controller, Listener, Key
from random import randrange
from multiprocessing import Process
import time

keyboard = Controller()

def on_press(key):
  random = randrange(20)
  if random == 0:
    keyboard.press('a')
  if random == 1:
    keyboard.press(Key.backspace)
  # try:
  #   print('alphanumeric key {0} pressed'.format(key.char))
  #   keyboard.press(key.char)
  # except AttributeError:
  #   print('special key {0}'.format(key))

def on_release(key):
  # try:
  #   print('{0} released'.format(key.char))
  #   # if key == keyboard.Key.esc:
  #   #   print('yup')
  #   #   return False
  # except AttributeError:
  #   print('special key {0}'.format(key))
  return

def shift_loop():
  print('running')
  while True:
    time.sleep(randrange(0, 1) + 1)
    keyboard.press(Key.shift)
    # keyboard.press('a')
    time.sleep(1)
    # keyboard.release('a')

def run_listener():
  with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

if __name__ == '__main__':
  p1 = Process(target=shift_loop).start()
  p2 = Process(target=run_listener).start()
