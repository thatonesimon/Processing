from zooming_circles import *
from config import *

add_library('minim')

def setup():
    size(window_size,window_size)
    

mode_counter = 0
def draw():
    mode = mode_counter%NUM_MODES
    if mode == ZOOM:
        zooming_circles()
    else:
        ellipse(centerX, centerY, 100, 100)

should_loop = True
def keyPressed():
    if key == ' ':
        global should_loop
        should_loop = not should_loop
        if should_loop:
            loop()
        else:
            noLoop()
    elif key == "a":
        global mode_counter
        mode_counter+=1
      
      
      
