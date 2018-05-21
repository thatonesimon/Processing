def setup():

    size(720, 720)
    # size(720, 720, OPENGL)
    colorMode(HSB, 11)
    
    global circles, triggered
    for i in range(total):
        circles.append(Circle())
        
    global x_step, y_step
    x_step = width/num_row
    y_step = height/num_col
    
    
def mouseClicked():
    
    x = mouseX/x_step
    y = mouseY/y_step
    circles[x+num_row*y].pulse = 10
    circles[x+num_row*y].triggered = 10
    
    
def center():
    
    # move to middle
    translate(width/2, height/2)
    # flip the y
    scale(1, -1)
    rotate(radians(-90))
    
num_row = 50
num_col = 50
total = num_row*num_col
circles = []
def draw():
    
    background(0)
    
    circleCheck()
    
    noFill()
    strokeWeight(100/num_row)
    for i in range(num_row):
        x = (i+0.5)*width/num_row
        for j in range(num_col):
            y = (j+0.5)*height/num_col
            stroke(circles[i+num_row*j].pulse, 10, 10)
            circle(x, y, 10+circles[i+num_row*j].pulse)
            
def circleCheck():
    global circles
    for i, c in enumerate(circles):

        if c.pulse > 0:
            c.pulse -= 0.5
            if c.pulse < 5:
                circles[(i-1)%total].shouldPulse()
                circles[(i+1)%total].shouldPulse()
                circles[(i-num_row)%total].shouldPulse()
                circles[(i+num_row)%total].shouldPulse()
                
def circle(x, y, rad):
    ellipse(x, y, rad*2, rad*2)
    
    
class Circle:
    
    def __init__(self):
        self.pulse = 0
        self.triggered = 0
        
    def shouldPulse(self):
        if self.triggered <= 0:
            self.pulse = 10
            self.triggered = 4
        else:
            self.triggered -= 1
