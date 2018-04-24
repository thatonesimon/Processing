window_size = 720
centerX = window_size/2
centerY = window_size/2

def setup():
    size(window_size,window_size)
    noLoop()
    
def draw():
    stroke(100)
    # fill(50)
    ellipse(centerX, centerY, 100, 100)
