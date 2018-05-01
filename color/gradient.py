from config import *

start_color = rand_color()
end_color = rand_color()
next_color = rand_color()

def vertical_grad():
    for i in xrange(window_height):
        c = start_color.gradient(end_color, i/(window_height*1.0)).to_color()
        for j in xrange(window_width):
            set(j, i, c)
            
def horizontal_grad():
    for i in xrange(window_width):
        c = start_color.gradient(end_color, i/(window_height*1.0)).to_color()
        for j in xrange(window_height):
            set(i, j, c)
            
grad = 0.1
grad_step = 0.005
def anim_vert_grad():
    global start_color, end_color, next_color, grad
    for y in xrange(window_height):
        c = start_color.gradient(end_color, y/(window_height*1.0)).to_color()
        for x in xrange(window_width):
            set(x, y, c)
            
    start_color = start_color.gradient(end_color, grad)
    end_color = end_color.gradient(next_color, grad)
    grad += grad_step
    if grad >= 1.0/3:
        start_color = end_color
        end_color = next_color
        next_color = rand_color()
        grad = 0.0
        
