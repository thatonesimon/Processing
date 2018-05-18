
COLORS = [
          
    color(255, 0, 0),
    color(0, 0, 0)
    
]

NUM_COLORS = len(COLORS)


square = []


def sqr(l):
    
    one = PVector(l, l)
    two = PVector(-l, l)
    three = PVector(-l, -l)
    four = PVector(l, -l)
        
    s = []
    s.append(one)
    s.append(two)
    s.append(three)
    s.append(four)
    
    return s

def tri(l):
    
    one = PVector(0, l)
    two = PVector(l*cos(radians(30)), l*-sin(radians(30)))
    three = PVector(l*-cos(radians(30)), l*-sin(radians(30)))
    
    s = []
    s.append(one)
    s.append(two)
    s.append(three)
    
    return s
            
        
