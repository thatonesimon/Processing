from config import *

from gradient import *
from blocks import *
from hsb import *

c_1 = rand_color()
c_2 = c_1.opposite()

def setup():
    size(window_width, window_height)
    background(0)
    # noLoop()

def draw():

    
    # vertical_grad()
    # horizontal_grad()
    # anim_vert_grad()
    
    # color_blocks(c_1, c_2)
    # moving_blocks()
    
    hsb_test()
    

def keyPressed():
    if key == ' ': draw()
