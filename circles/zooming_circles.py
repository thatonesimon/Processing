from config import *

# circle definitions
rad_step = 50
radius = 100
angle = 0

def zooming_circles():
    global r, g, b, radius, angle
    # background(1,1,1)
    r = 255*sin(angle)%255
    for i in reversed(xrange(25)):
        # fill(r+5*i, g*i, b*i)
        ellipse(centerX, centerY, (radius+rad_step*i)%1250, (radius+rad_step*i)%1250)
    radius+=1
    if radius > rad_step:
        radius = 0
    angle+=0.01
