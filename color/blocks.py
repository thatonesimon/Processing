from config import *

num_blocks = 10

def color_blocks(s, e):
    step = 0
    for i in xrange(num_blocks):
        c = s.gradient(e, i / (num_blocks - 1.0)).to_color()
        for row in xrange(int(window_width / num_blocks)):
            for column in xrange(int(window_height)):
                set(row + step, column, c)
        step += int(window_width / num_blocks)


c_1 = rand_color()
c_2 = rand_color()
offset = 0
def moving_blocks():
    global offset
    step = offset
    for i in xrange(num_blocks):
        c = c_1.gradient(c_2, i / (num_blocks - 1.0)).to_color()
        for row in xrange(int(window_width / num_blocks)):
            for column in xrange(int(window_height)):
                set(row + step, column, c)
        step += int(window_width / num_blocks)
    offset = (offset+1)%int(window_width / num_blocks)
    
    
setup = False
def setup_moving_blocks():
    global setup
    if not setup:
        setup = True
