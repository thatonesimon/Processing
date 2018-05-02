from config import *

# point definitions
points = []
layers = 3
layer_size = 50
num_points = 6
step = 2*PI/num_points
radius = 100
dot_size = 5
angle = 0
direction = 1


def trace_circle():
    global num_points, step, angle, distance, dist_step, direction
    
    circle_setup()
    background(0)
    
    stroke(255)
    for layer in xrange(layers):
        for i in xrange(num_points):
            x = centerX + (radius+layer*layer_size)*cos(angle+i*step)
            y = centerY + direction*(radius+layer*layer_size)*sin(angle+i*step)
            # ellipse(centerX + radius*cos(angle+i*step), centerY + radius*sin(angle+i*step), dot_size, dot_size)
            # ellipse(centerX + (radius+i*layer_size)*cos(angle+i*step), centerY + (radius+i*layer_size)*sin(angle+i*step), dot_size, dot_size)
            ellipse(x, y, dot_size, dot_size)
        angle += 0.01
        direction = -direction
        
    
    
setup = False
def circle_setup():
    global setup
    if not setup:
        setup = True
