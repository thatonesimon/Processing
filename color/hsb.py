from config import *

def hsb_test():
    noStroke()
    colorMode(HSB, window_width)
    for i in range(window_width): 
        for j in range(window_height): 
            stroke(i, j, window_width)
            point(i, j)
            
cur_hue = 0.0
def hsb_morph():
    global cur_hue
    colorMode(HSB, 100)
    background(cur_hue%100, 100, 100)
    textSize(32)
    text(str((cur_hue%100)), 10, 30)
    # fill(0, 102, 153)
    cur_hue += 0.5
