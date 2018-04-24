window_size = 720
centerX = window_size/2
centerY = window_size/2

r = 30
g = 20
b = 10

rad_step = 50
radius = 100
angle = 0

def setup():
    size(window_size,window_size)
    
def draw():
    global r, g, b, radius, angle
    # background(1,1,1)
    r = 255*sin(angle)%255
    for i in reversed(xrange(25)):
        fill(r+5*i, g*i, b*i)
        ellipse(centerX, centerY, (radius+rad_step*i)%1250, (radius+rad_step*i)%1250)
    radius+=1
    if radius > rad_step:
        print "rad"
        radius = 0
    angle+=0.01

should_loop = True
def keyPressed():
  if key == ' ':
      global should_loop
      should_loop = not should_loop
      if should_loop:
        loop()
      else:
        noLoop()
