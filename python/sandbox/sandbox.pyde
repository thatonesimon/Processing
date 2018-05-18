from config import *

def setup():

    size(720, 720)
    # size(720, 720, OPENGL)
    
def center():
    
    # move to middle
    translate(width/2, height/2)
    # flip the y
    scale(1, -1)
    
    
seed_x = 0
seed_y = 0
seed_rad = 620
seed_angle = 0
num_points = 5
point_step = 360/num_points
def draw():
    
    background(0)
    
    center()
    
    global seed_x, seed_y, seed_rad, seed_angle
    
    stroke(255)
    noFill()
    circle(seed_x, seed_y, seed_rad)
    
    inner_shape = []
    for i in range(num_points):
        
        x = seed_rad*cos(radians(i*point_step+seed_angle))/2
        y = seed_rad*sin(radians(i*point_step+seed_angle))/2
        inner_shape.append(PVector(x, y))
        
    inner_inner_shape = []
    last = inner_shape[len(inner_shape)-1]
    beginShape()
    for p in inner_shape:
        vertex(p.x, p.y)
        old_p = p.copy()
        p.sub(last)
        last = old_p
        
    endShape(CLOSE)
    
    # beginShape()
    # for p in inner_shape:
    #     vertex(p.x, p.y)
    #     p.sub(last)
    #     last = p
        
    # endShape(CLOSE)
    
    
    
    seed_angle += 1

    
    
def circle(x, y, rad):
    
    stroke(255, 255, 255)
    ellipse(x, y, rad, rad)


    
