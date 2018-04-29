# vars for window coordinates
window_width = 720
window_height = 720
centerX = window_width / 2
centerY = window_height / 2

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
        
    def to_white(self, percent):
        return self.gradient(WHITE, percent)
    
    def to_black(self, percent):
        return self.gradient(BLACK, percent)
    
    def to_color(self):
        return color(self.r, self.g, self.b)
    
    def to_hex(self):
        # return '#%02x%02x%02x' % (self.r, self.g, self.b)
        return int(self.r*16^4 + self.g*16^2 + self.b)
    
    def gradient(self, c2, percent):
        dr = c2.r - self.r
        dg = c2.g - self.g
        db = c2.b - self.b
        r = self.r + dr*percent
        g = self.g + dg*percent
        b = self.b + db*percent
        grad_color = Color(r, g, b)
        return grad_color

WHITE = Color(255, 255, 255)
BLACK = Color(0, 0, 0)
