from config import *

def setup():
    
    size(720, 720, OPENGL)
    frameRate(30)
    # noLoop()
    noStroke()

def moveCenter():
    background(100)
    translate(width/2, height/2)
    rotate(radians(180))
    # scale(100, 100)
    
    
base_rot = 0
num_layers = 1
step = 0.5
def draw():
    
    moveCenter()
    
    beginShape()
    
    fill(COLORS[0])
    # shape = tri(width)
    shape = sqr(width/2)
    
    for p in shape:
        vertex(p.x, p.y)

    endShape(CLOSE)
    
    drawInside(shape, 1)
    
    global inside_delta
    inside_delta += 0.1
    
    
    

max_iter = 50
inside_delta = 0
def drawInside(shape, iter):
    
    if iter > max_iter:
        return
    
    shape_delta = []
    
    # fill(iter*255/max_iter+50)
    fill(COLORS[iter%NUM_COLORS])
    
    for p in shape:
        
        p_cpy = p.copy()
        shape_delta.append(p_cpy)
        
    last = shape[len(shape)-1]
    for i, p in enumerate(shape_delta):
        # experiment with THIS line!
        # p.sub(last).mult(0.5)
        p.sub(last).mult(0.01*(inside_delta%100))
        last = shape[i]
        
    beginShape()
    for i, p in enumerate(shape):
        p.sub(shape_delta[i])
        vertex(p.x, p.y)
        
    endShape(CLOSE)
    
    drawInside(shape, iter+1)
        
        
    
        
