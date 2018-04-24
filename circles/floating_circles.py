from config import *

setup = False

# circle definitions
rad_step = 50
radius = 100
angle = 0
num_circles = 10

# circle: [x, y, upwards force]
circles = []

def floating_circles():
    float_setup()
    global circles
    for i in xrange(num_circles):
        ellipse(circles[i][0], circles[i][1], 100, 100)
        circles[i][1] -= circles[i][2] * 10
        if circles[i][1] <= -radius:
            circles[i][0] = random(0, window_width)
            circles[i][1] = window_height + radius
            circles[i][2] = random(1)
    
def float_setup():
    global setup
    if not setup:
        for i in xrange(num_circles):
            x = random(0, window_width)
            y = window_height + radius
            upwards = random(1)
            circles.append([x,y, upwards])
        setup = True
