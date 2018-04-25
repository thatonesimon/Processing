from config import *

setup = False

# circle definitions
rad_step = 50
radius = 100
angle = 0
num_circles = 25

min_rad = 50
max_rad = 100
min_dy = 1
max_dy = 5

circles = []

def floating_circles():
    float_setup()
    global circles
    for c in circles:
        stroke(c.color.r, c.color.g, c.color.b, 255*c.y/height)
        fill(c.color.r, c.color.g, c.color.b, 255*c.y/height)
        ellipse(c.x, c.y, c.radius, c.radius)
        # ellipse(width-c.x, height-c.y, c.radius, c.radius)
        c.y += c.dy
        if c.y <= -c.radius:
            reset_circle(c)
    
def float_setup():
    global setup
    if not setup:
        for i in xrange(num_circles):
           create_circle()
        setup = True
        
def create_circle():
    x = random(0, width)
    start_radius = random(min_rad, max_rad)
    y = height + start_radius
    dy = -random(min_dy, max_dy)
    new_circle = Circle(x, y, start_radius, 0, dy, random(255), random(255), random(255))
    circles.append(new_circle)
    
def create_circle(x, y):
    start_radius = random(min_rad, max_rad)
    dy = -random(min_dy, max_dy)
    new_circle = Circle(x, y, start_radius, 0, dy, random(255), random(255), random(255))
    circles.append(new_circle)
    
def reset_circle(c):
    c.x = random(0, width)
    c.radius = random(min_rad, max_rad)
    c.y = height + radius
    c.dy = -random(min_dy, max_dy)
    
def mouseClicked():
    create_circle(mouseX, mouseY)
