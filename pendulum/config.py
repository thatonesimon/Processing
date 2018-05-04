# vars for window coordinates
window_width = 1080
window_height = 720
centerX = window_width / 2
centerY = window_height / 2

class Color:
    h = 0
    s = 0
    b = 0
    
    def __init__(self, h, s, b):
        self.h = h
        self.s = s
        self.b = b
        
    def asColor(self):
        return color(self.h, self.s, self.b)

class Circle:
    x = 0
    y = 0
    radius = 25
    color = Color(0, 0, 0)
        
    def __init__(self, x, y, radius, h = 255, s = 50, b = 100):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = Color(h, s, b)
    
    def draw(self, pulse = 0):
        fill(self.color.asColor())
        ellipse(self.x, self.y, self.radius + pulse, self.radius + pulse)
