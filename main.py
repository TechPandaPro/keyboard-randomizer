from pynput.keyboard import Controller, Listener, Key
from random import choice, randrange
from multiprocessing import Process
import time

keyboard = Controller()

keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def on_press(key):
  random = randrange(20)
  if random == 0:
    keyboard.press(choice(keys))
  if random == 1:
    keyboard.press(Key.backspace)

def shift_loop():
  print('running')
  while True:
    time.sleep(randrange(0, 1) + 1)
    keyboard.press(Key.shift)
    time.sleep(1)

def run_listener():
  with Listener(on_press=on_press) as listener:
    listener.join()

if __name__ == '__main__':
  p1 = Process(target=shift_loop).start()
  p2 = Process(target=run_listener).start()
