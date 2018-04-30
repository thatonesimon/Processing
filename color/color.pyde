from config import *

from gradient import *
from blocks import *

c_1 = rand_color()
c_2 = rand_color()

def setup():
    size(window_width, window_height)
    background(0)
    # noLoop()

def draw():

    
    # vertical_grad()
    # horizontal_grad()
    anim_vert_grad()
    
    # color_blocks(c_1, BLACK)
    moving_blocks()
    

def keyPressed():
    if key == ' ': draw()
