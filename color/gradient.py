from config import *

def vertical_grad(start_color, end_color):
    for i in xrange(window_height):
        c = start_color.gradient(end_color, i/(window_height*1.0)).to_color()
        for j in xrange(window_width):
            set(j, i, c)
            
def horizontal_grad(start_color, end_color):
    for i in xrange(window_width):
        c = start_color.gradient(end_color, i/(window_height*1.0)).to_color()
        for j in xrange(window_height):
            set(i, j, c)
