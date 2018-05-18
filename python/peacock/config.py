

class Feather:
    
    def __init__(self, len, size):
        self.len = len
        self.size = size
        
    def show(self):
        
        strokeWeight(2)
        stroke(255)
        
        pushMatrix()

        # line(0, 0, self.len, 0)
        
        noStroke()
        fill(2, 5, 86)
        ellipse(self.len, 0, self.size*5, self.size*5)
        
        fill(1, 172, 212)
        ellipse(self.len, 0, self.size*4, self.size*4)
        
        fill(178, 127, 37)
        ellipse(self.len, 0, self.size*2.5, self.size*2.5)
        
        fill(12, 166, 134)
        ellipse(self.len, 0, self.size*1, self.size*1)
        
        popMatrix()
