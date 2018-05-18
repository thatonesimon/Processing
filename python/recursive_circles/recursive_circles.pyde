
def setup():

    size(720, 1080)
    # size(720, 720, OPENGL)
    noLoop()
    
    
def center():
    
    translate(width/2, height/2)
    rotate(radians(45))
    translate(-200, -200)
    
    
seed_rad = 2000
seed_x = 0
def draw():
    
    background(0)
    
    center()
    
    global seed_rad, seed_x
    
    stroke(255)
    noFill()
    circle(seed_x, 0, seed_rad)
    
    seed_rad += 100
    
    if seed_rad > 2000:
        seed_rad = 1000
    seed_rad += 1.0
    
    
def circle(x, y, rad):
    
    # strokeWeight(2)
    
    stroke(x, y, x+y, 255*rad/100+50)
    ellipse(x, y, rad, rad)

    if rad > 10:
        circle(x-rad/4, y, rad*0.5)
        circle(x+rad/4, y, rad*0.5)
        circle(x, y-rad/4, rad*0.5)
        circle(x, y+rad/4, rad*0.5)
    
