from config import *

def hsb_test():
    colorMode(HSB, window_width)
    for i in range(window_width): 
        for j in range(window_height): 
            stroke(i, j, window_width)
            point(i, j)
