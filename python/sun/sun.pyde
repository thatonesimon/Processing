from config import *

import random

def setup():
    
    size(720, 480, P2D)
    frameRate(5)
    
    
num_rays = 20
ray_size = 180.0/(num_rays-1)
    
def draw():
    
    translate(width/2, height)
    background(0)
    

    noStroke()
    rotate(radians(180))
    last = None
    
    for i in range(num_rays):
        c = random.randint(0, len(RAY_COLORS)-1)
        while c == last:
            c = random.randint(0, len(RAY_COLORS)-1)
        
        fill(RAY_COLORS[c])
        last = c
            
        
        beginShape()
        vertex(0, 0)
        vertex(width, 0)
        vertex(width*cos(radians(ray_size)), width*sin(radians(ray_size)))
        endShape(CLOSE)
        rotate(radians(ray_size))
        
        
    strokeWeight(1)
    stroke(255)
    fill(RAY_COLORS[4])
    ellipse(0, 0, 200, 200)
    
    noStroke()
    fill(RAY_COLORS[3])
    ellipse(0, 0, 150, 150)
    fill(RAY_COLORS[2])
    ellipse(0, 0, 100, 100)
