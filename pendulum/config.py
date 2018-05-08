# vars for window coordinates
window_width = 1080
window_height = 720
centerX = window_width / 2
centerY = window_height / 2

class Color:
    h = 0
    s = 0
    b = 0
    a = 100
    
    def __init__(self, h, s, b):
        self.h = h
        self.s = s
        self.b = b
        
    def asColor(self):
        return color(self.h, self.s, self.b, self.a)

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
        stroke(0, 0, 0, self.color.a)
        fill(self.color.asColor())
        ellipse(self.x, self.y, self.radius + pulse, self.radius + pulse)
        
# group of objects that moves around in circle
class CircleGroup:
    
    cen_x = 0
    cen_y = 0
    
    radius = 0
    angle = 0
    
    circles = []
    num_circles = 0
    
    def __init__(self, cen_x, cen_y, radius = 0, angle = 0):
        self.cen_x = cen_x
        self.cen_y = cen_y
        self.radius = radius
        self.angle = angle
        
    def add(self, c):
        self.circles.append(c)
        self.num_circles += 1
        
    def draw(self, pulse = 0):
        for c in circles:
            ellipse(c.x+self.x, c.y+self.y, c.radius + pulse, c.radius + pulse)
    
