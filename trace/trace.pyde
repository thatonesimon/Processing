from config import *

from trace_circle import *
from two_circles_one_line import *
from generate_circles import *
from generate_line import *
from generate_grid import *

def setup():
    size(window_width,window_height)
    background(0)
    
mode_counter = 0
def draw():

    # trace_circle()
    # draw_lines()
    # generate_arcs()
    # generate_worms()
    generate_grid()
    
def mouseClicked():
    add_point(mouseX, mouseY)
    
def keyPressed():
    
    if key == " ":
        reset_grid()
