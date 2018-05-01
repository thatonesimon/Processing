from config import *

angle = 0.0
angle_step = 0.1
radius = 50.0
max_radius = 100
dot_size = 1.0
dir = -1

center = Point(centerX, centerY)
cur = Point(0, 0)

c = Color(255, 255, 255)

def generate_arcs():
    global angle, radius, p
    
    stroke(255)
    if dir == CLOCKWISE:
        cur.x = center.x + dir*radius*cos(angle)
        cur.y = center.y + dir*radius*sin(angle)
    else:
        cur.x = center.x + dir*radius*sin(angle)
        cur.y = center.y + dir*radius*cos(angle)
    ellipse(cur.x, cur.y, dot_size, dot_size)
    angle += angle_step
    if angle%2*PI >= PI:
        if random(10) > 5:
            randomize()
            angle = (angle+PI)%(2*PI)
    
    
def randomize():
    global radius, center, dir
    
    new_radius = random(10, 100)
    dx = (cur.x - center.x)/radius
    dy = (cur.y - center.y)/radius
    center.x = cur.x + dx*new_radius
    center.y = cur.y + dy*new_radius
    radius = new_radius
    dir = -dir
    
