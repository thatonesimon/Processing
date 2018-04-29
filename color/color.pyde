from config import *

from gradient import *
from blocks import *

start_color = Color(100, 150, 200)
end_color = Color(200, 150, 100)

def setup():
    size(window_width, window_height)
    # noLoop()

def draw():
    background(0)
    
    # vertical_grad(start_color, end_color)
    # horizontal_grad(start_color, end_color)
    
    # color_blocks(start_color, BLACK)
    moving_blocks()
    

def keyPressed():
    if key == ' ': draw()
