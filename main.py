from pynput.keyboard import Controller, Listener
import time

keyboard = Controller()

listener = None

def on_press(key):
  global listener

  try:
    print('alphanumeric key {0} pressed'.format(key.char))
    listener.stop()
    listener = None
    print(key.char)
    keyboard.press(key.char)
  except AttributeError as error:
    print('special key {0}'.format(key))

def on_press_no_suppress(key):
  if not listener:
    create_listener()

def create_listener():
  global listener
  listener = Listener(on_press=on_press)
  listener.start()

listener_no_suppress = Listener(on_press=on_press_no_suppress)
listener_no_suppress.start()

create_listener()

# prevent program from exiting
while True:
  time.sleep(5)
