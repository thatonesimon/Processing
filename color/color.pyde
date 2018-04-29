from config import *

start_color = Color(100, 150, 200)

def setup():
    size(window_width, window_height)
    noLoop()

def draw():
    background(0)
    for i in xrange(window_width):
        for j in xrange(window_height):
            set(i, j, start_color.to_black(j/(window_height*1.0)).to_color())
    print "done"
    

def keyPressed():
    if key == 'k': print k
