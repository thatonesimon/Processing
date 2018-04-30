from config import *

num_points = 10
dot_size = 10.0

points = []
dx = 0.0
dy = 0.0
d = 1.0

def generate_lines():
    global dx, dy, dot_size, points
    
    gen_line_setup()
    # background(0)
    for p in points:
        # stroke(c.r, c.g, c.b)
        cur_stroke = p.c.to_black(1 - 10.0/p.size)
        stroke(cur_stroke.r, cur_stroke.g, cur_stroke.b) 
        fill(p.c.r, p.c.g, p.c.b)
        ellipse(p.x, p.y, p.size, p.size)
        p.dx += random(-d, d)
        p.dy += random(-d, d)
        p.x += p.dx
        p.y += p.dy
        p.size += 0.5
    
        if p.x-p.size > width or p.x+p.size < 0 or p.y-p.size > width or p.y+p.size < 0:
            p.x = centerX
            p.y = centerY
            p.dx = 0
            p.dy = 0
            p.size = 10.0
            p.c.lite_randomize()
            
setup = False
def gen_line_setup():
    global setup
    if not setup:
        for i in xrange(num_points):
           add_point(centerX, centerY)
        setup = True
        
def add_point(x, y):
    global points
    p = Point(x, y)
    points.append(p)
