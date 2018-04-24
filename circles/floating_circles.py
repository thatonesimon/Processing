from config import *

# circle definitions
rad_step = 50
radius = 100
angle = 0

y = window_size

def floating_circles():
    global y
    ellipse(centerX, y, 100, 100)
    y-=1
