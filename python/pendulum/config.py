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
        
    def __init__(self, x, y, radius, h = 100, s = 50, b = 100):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = Color(h, s, b)
    
    def draw(self, pulse = 0):
        # stroke(0, 0, 0, self.color.a)
        fill(self.color.asColor())
        ellipse(self.x, self.y, self.radius + pulse, self.radius + pulse)
        
# group of objects that moves around in circle
class Flower:
    
    x = 0
    y = 0
    radius = 0
    flower_angle = 0
    num_petals = 5
    petal_size = 10
    color = None
    dir = 1
    
    def __init__(self, x, y, flower_angle, color, dir):
        self.x = x
        self.y = y
        self.flower_angle = flower_angle
        self.color = color
        self.dir = dir
        
    def draw(self, spiral_angle = 0):
        stroke(0, 0, 0, self.color.a)
        fill(self.color.h, self.color.s, self.color.b, self.color.a)
        
        self.flower_angle += 2*PI/self.num_petals
        
        for i in range(self.num_petals):
            x = self.x + self.radius*cos(self.dir*(self.flower_angle + spiral_angle))
            y = self.y + self.radius*sin(self.dir*(self.flower_angle + spiral_angle))
            ellipse(x, y, self.petal_size, self.petal_size)
            self.flower_angle += 2*PI/self.num_petals
            
        self.flower_angle += 0.01
        self.radius += 1
        self.petal_size += 2.0/self.num_petals
        self.color.a -= 0.5
            
        
            
