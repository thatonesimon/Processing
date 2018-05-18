from config import *

def setup():
    
    size(720, 720, OPENGL)
    frameRate(30)
    noLoop()

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

    # global base_rot, layer_scale, layer_rot
    # rotate(radians(base_rot))
    
    # for layer in reversed(range(num_layers)):
    #     fill(COLORS[layer%NUM_COLORS])
    #     beginShape()
        
    #     stroke(0)
    #     strokeWeight(1)
        

    #     vertex(one.x, one.y)
    #     vertex(two.x, two.y)
    #     vertex(three.x, three.y)

    #     endShape(CLOSE)
    
    
    
    beginShape()
    
    stroke(0)
    strokeWeight(1)
    
    shape = tri(width)
    shape = sqr(width/2)
    
    for p in shape:
        vertex(p.x, p.y)

    endShape(CLOSE)
    
    drawInside(shape, 1)
    
    
    

max_iter = 50
def drawInside(shape, iter):
    
    if iter > max_iter:
        return
    
    shape_delta = []
    # noStroke()
    
    fill(iter*255/max_iter+50)
    
    for p in shape:
        
        p_cpy = p.copy()
        shape_delta.append(p_cpy)
        
    last = shape[len(shape)-1]
    for i, p in enumerate(shape_delta):
        # experiment with THIS line!
        # p.sub(last).mult(0.5)
        p.sub(last).mult(1.0/iter)
        last = shape[i]
        
    beginShape()
    for i, p in enumerate(shape):
        p.sub(shape_delta[i])
        vertex(p.x, p.y)
        
    endShape(CLOSE)
    
    drawInside(shape, iter+1)
        
        
    
        
