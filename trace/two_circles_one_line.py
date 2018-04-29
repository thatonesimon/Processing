from config import *

c1_rad = 400
c2_rad = 200
angle = 0

num_lines = 6

def draw_lines():
    global angle
    
    # background(0)
    fill(0)
    stroke(255)
    # ellipse(centerX, centerY, c1_rad, c1_rad)
    # ellipse(centerX, centerY, c2_rad, c2_rad)
    
    for i in xrange(num_lines):
        c1_point = c1(angle+0.1*i)
        c2_point = c2(angle+0.1*i)
        line(c1_point[0], c1_point[1], c2_point[0], c2_point[1])
        
    angle += 0.01
    
    
    
def c1(x):
    return (c1_rad*cos(x)/2+centerX, c1_rad*sin(x)/2+centerY)

def c2(x):
    return (c2_rad*cos(x)/2+centerX, c2_rad*sin(x)/2+centerY)
