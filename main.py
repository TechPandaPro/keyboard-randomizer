from pynput.keyboard import Controller as KeyboardController, Listener as KeyboardListener, Key
from pynput.mouse import Controller as MouseController, Listener as MouseListener, Button
from multiprocessing import Process
import random
import time

keyboard = KeyboardController()
mouse = MouseController()

keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def on_press(key):
  randomNum = random.randrange(20)
  if randomNum == 0:
    keyboard.press(random.choice(keys))
  if randomNum == 1:
    keyboard.press(Key.backspace)

currently_moving = False
moving_since = None

def on_move(x, y):
  global currently_moving
  global moving_since
  global move_x
  global move_y

  if currently_moving:
    if moving_since + 0.3 < time.time():
      currently_moving = False
      moving_since = None
      move_x = None
      move_y = None
    else:
      move_x = random.uniform(-1, 1)
      move_y = random.uniform(-1, 1)
      mouse.move(move_x, move_y)
  elif random.randrange(500) == 0:
    currently_moving = True
    moving_since = time.time()

def mouse_random():
  mouse.click(Button.left)
  if random.randrange(5) == 0:
    mouse.scroll(random.uniform(-50, 50), random.uniform(-50, 50))

def on_scroll(x, y, dx, dy):
  mouse_random()

# def mouse_loop():
#   while True:
#     time.sleep(random.randrange(0, 10) + 1)
#     mouse_random()
    
def run_keyboard_listener():
  with KeyboardListener(on_press=on_press) as listener:
    listener.join()

def run_mouse_listener():
  with MouseListener(on_move=on_move, on_scroll=on_scroll) as listener:
    listener.join()

if __name__ == '__main__':
  # p1 = Process(target=mouse_loop).start()
  p2 = Process(target=run_keyboard_listener).start()
  p2 = Process(target=run_mouse_listener).start()
