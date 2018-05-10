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
        stroke(0, 0, 0, self.color.a)
        fill(self.color.asColor())
        ellipse(self.x, self.y, self.radius + pulse, self.radius + pulse)
        
# group of objects that moves around in circle
class Flower:
    
    x = 0
    y = 0
    radius = 0
    num_petals = 0
    petal_size = 0
    color = None
    
    def __init__(self, x, y, radius, num_petals, petal_size, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.num_petals = num_petals
        self.petal_size = petal_size
        self.color = color
        
    def draw(self, spiral_angle = 0):
        
        fill(self.color.h, self.color.s, self.color.b, self.color.a)
        
        flower_angle += 2*PI/num_flowers
        
        for i in range(num_petals):
            x = self.x + self.radius*cos(flower_angle + spiral_angle)
            y = self.y + self.radius*sin(flower_angle + spiral_angle)
            ellipse(x, y, self.petal_size, self.petal_size)
            flower_angle += 2*PI/self.num_petals
            
        
            
