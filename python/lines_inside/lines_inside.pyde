
def setup():

    size(720, 720)
    # size(720, 720, OPENGL)
    # colorMode(HSB, 256)
    
def keyPressed():
    
    # left
    if keyCode == 37:
        global inside_delta
        inside_delta -= 0.1
        
    # right
    elif keyCode == 39:
        global inside_delta
        inside_delta += 0.1
    
    
def center():
    
    # move to middle
    translate(width/2, height/2)
    # flip the y
    scale(1, -1)
    rotate(radians(-90))
    
    
x = 0
y = 0
radius = 720/2
angle = 0
num_lines = 1
line_step = 360.0/num_lines
clock = 0
counter = 0
def draw():
    
    background(0)
    
    center()
    
    global x, y, radius, angle, clock, counter, num_lines, line_step
    
    stroke(0)
    circle(x, y, radius)

    
    strokeWeight(2)
    for i in range(num_lines):
        
        p1 = PVector(radius*cosr(clock+(i*line_step)), radius*sinr(clock+(i*line_step)))
        p2 = PVector(radius*cosr(counter+(i*line_step)), radius*sinr(counter+(i*line_step)))
        # stroke(COLORS[i%NUM_COLORS])
        line(p1.x, p1.y, p2.x, p2.y)
        # ellipse(p1.x, p1.y, 20, 20)
        # ellipse(p2.x, p2.y, 20, 20)

    clock += 1.0
    counter -= 1.0
    
    if clock%180 == 0:
        num_lines += 1
        line_step = 360.0/num_lines
    
def circle(x, y, rad):
    ellipse(x, y, rad*2, rad*2)
  
def sinr(angle):
    return sin(radians(angle))

def cosr(angle):
    return cos(radians(angle))

    
