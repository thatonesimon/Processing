# vars for window coordinates
window_width = 720
window_height = 720
centerX = window_width / 2
centerY = window_height / 2

# base RGB values
r = 30
g = 20
b = 10

# mode def
NUM_MODES = 2
ZOOM = 0
FLOAT = 1

class Color:
    r = 0
    g = 0
    b = 0
    
    def __init__(self, r = None, g = None, b = None):
        if r is None or g is None or b is None:
            self.r = random(255)
            self.g = random(255)
            self.b = random(255)
        else:
            self.r = r
            self.g = g
            self.b = b
            
    def __str__(self):
        return "(" + str(self.r) + "," + str(self.g) + "," + str(self.b) + ")"
        
    def randomize(self):
        self.r = random(255)
        self.g = random(255)
        self.b = random(255)

class Circle:
    x = 0
    y = 0
    dx = 0
    dy = 0
    radius = 25
    color = Color(0, 0, 0)
        
    def __init__(self, x, y, radius, dx = 0, dy = 0, r = 255, g = 255, b = 255):
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = dx
        self.dy = dy
        self.color = Color(r, g, b)
    
    def draw(self):
        ellipse(self.x, self.y, self.radius, self.radius)
        
        
def gradient(c1, c2, percent):
    dr = abs(c1.r - c2.r)
    dg = abs(c1.g - c2.g)
    db = abs(c1.b - c2.b)
    r = dr*percent + min(c1.r, c2.r)
    g = dg*percent + min(c1.g, c2.g)
    b = db*percent + min(c1.b, c2.b)
    grad_color = Color(r, g, b)
    return grad_color
