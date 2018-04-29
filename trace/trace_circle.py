from config import *

# point definitions
points = []
num_points = 1
step = 2*PI/num_points
radius = 5
angle = 0
distance = 0.0
max_dist = 200.0
dist_step = 25.0


def trace_circle():
    global num_points, step, angle, distance, dist_step
    
    circle_setup()
    background(0)
    
    stroke(255)
    for i in xrange(num_points):
        ellipse(centerX + distance*cos(angle+i*step), centerY + distance*sin(angle+i*step), radius, radius)
    angle += 0.01
    distance += dist_step
    if distance > max_dist or distance < 0:
        dist_step = -dist_step
    if distance < 0:
        num_points += 1
        step = 2*PI/num_points
        
    
    
setup = False
def circle_setup():
    global setup
    if not setup:
        setup = True
