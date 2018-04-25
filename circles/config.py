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
    
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

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
