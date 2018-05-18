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
        
    #     one = PVector(0, 100)
    #     two = PVector(100*cos(radians(30)), 100*-sin(radians(30)))
    #     three = PVector(100*-cos(radians(30)), 100*-sin(radians(30)))
    #     vertex(one.x, one.y)
    #     vertex(two.x, two.y)
    #     vertex(three.x, three.y)

    #     endShape(CLOSE)
        
    #     d1 = two.sub(one).mult(0.5)
    #     d2 = three.sub(two)
    #     d3 = one.sub(three)
        
    #     # print d1
        
    #     inside1 = one.add(d1)
    #     # inside2 = two.add(d2)
    #     # inside3 = three.add(d3)
        
    #     print inside1
        
    #     # beginShape()
    #     # fill(0)
    #     # vertex(inside1.x, inside1.y)
    #     # vertex(inside2.x, inside2.y)
    #     # vertex(inside3.x, inside3.y)
    #     # endShape(CLOSE)
    
    
    
    
    beginShape()
    
    stroke(0)
    strokeWeight(1)
    
    l = 100
    one = PVector(l, l)
    two = PVector(-l, l)
    three = PVector(-l, -l)
    four = PVector(l, -l)
    
    print two
        
    ps = []
    ps.append(one)
    ps.append(two)
    ps.append(three)
    ps.append(four)
    
    for p in ps:
        vertex(p.x, p.y)

    endShape(CLOSE)
    
    s = 1.0
    d1 = two.sub(one).mult(s)
    d2 = three.sub(two).mult(s)
    d3 = four.sub(three).mult(s)
    d4 = one.sub(four).mult(s)
    
    print two

    new1 = one.add(d1)
    new2 = two.add(d2)
    new3 = three.add(d3)
    new4 = four.add(d4)
    
    newps = []
    newps.append(new1)
    newps.append(new2)
    newps.append(new3)
    newps.append(new4)
    
    beginShape()
    for p in newps:
        vertex(p.x, p.y)

    endShape(CLOSE)
    
    
        
        
        
    
        
