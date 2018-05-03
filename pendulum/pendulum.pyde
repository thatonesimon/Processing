from config import *

def setup():
    size(window_width, window_height)
    colorMode(HSB, 100)
    background(100, 0, 100)
    # frameRate(1)
    global hand, head
    hand = loadImage("res/hand.png")
    head = loadImage("res/head.png")
    
def draw():
    global string_end, cur_angle, cur_hue, direction, gravity, gravity_dir, speed
    
    background(100-cur_hue%100, 50, 100)
    drawRings()
    drawHand()
    drawHead()
    string_end[0] = string_start[0] + string_len*cos(cur_angle)
    string_end[1] = string_start[1] + string_len*sin(cur_angle)
    
    drawString()
    drawPen()
    
    next_angle = cur_angle + speed

    # # if passing by bottom of swing leftwards
    # if next_angle - cur_angle > 0 and cur_angle > PI/2:
    #     gravity_dir = -1
    
    # # if passing by bottom of swing rightwards
    # elif next_angle - cur_angle < 0 and cur_angle < PI/2:
    #     gravity_dir = -1
        
    # if reach max left or right
    # TODO: count only the max hit
    # if cur_angle < PI/4:
    #     print "Hit right"
    # if cur_angle > 3*PI/4:
    #     print "Hit left"
        
    # if reaching bottom from right to left <-
    if cur_angle < PI/2 and next_angle > PI/2:
        # print "Sweep right to left"
        gravity *= -1
    # if reaching bottom from left to right ->
    if cur_angle > PI/2 and next_angle < PI/2:
        # print "Sweep left to right"
        gravity *= -1
    
    cur_angle = next_angle
    
    next_speed = speed+weight*gravity*gravity_dir
    # print degrees(cur_angle)
    if speed >= 0 and next_speed < 0:
        # print "Hit left " + str(PI/2-cur_angle)
        addRing()
    if speed <= 0 and next_speed > 0:
        # print "Hit right " + str(PI/2-cur_angle)
        addRing()
    speed = next_speed
    
    cur_hue += 0.1
    
def mouseClicked():
    print mouseX
    print mouseY
    
def keyPressed():
    print keyCode
    # UP
    if keyCode == 38:
        global string_len
        string_len -= 3
    # DOWN
    elif keyCode == 40:
        global string_len
        string_len += 3
    # LEFT
    elif keyCode == 37:
        global speed
        speed += gravity
    # RIGHT
    elif keyCode == 39:
        global speed
        speed -= gravity
        
def drawHand():
    tint(cur_hue%100, 50, 100)
    image(hand, centerX-140, 95)
    
def drawHead():
    tint(cur_hue, 50, 100)
    image(head, centerX-100, 7*window_height/10, 200, 200*head.height/head.width)

string_len = 300
string_start = [centerX, 200]
string_end = [0, 0]
def drawString():
    stroke(0)
    line(string_start[0], string_start[1], string_end[0], string_end[1])

pen_size = 50
cur_angle = PI/8
cur_hue = 0.0
direction = 1
gravity = 0.001
gravity_dir = 1
speed = 0.0
weight = 1.0
def drawPen():
    fill(cur_hue%100, 50, 100)
    drawTail()
    stroke(0)
    ellipse(string_end[0], string_end[1], pen_size, pen_size)
    
num_trails = 7
def drawTail():
    noStroke()
    for i in reversed(xrange(num_trails)):
        fill(cur_hue%100, 50, 100, 100-100*i/num_trails)
        trail_center = [None, None]
        trail_center[0] = string_start[0] + string_len*cos(cur_angle-i*speed)
        trail_center[1] = string_start[1] + string_len*sin(cur_angle-i*speed)
        ellipse(trail_center[0], trail_center[1], pen_size-5*i, pen_size-5*i)
    
    
rings = []
ring_hue = 0.0
max_rings = 15
def addRing():
    global rings, ring_hue
    new_ring = [string_end[0], string_end[1], pen_size, 100-cur_hue%100]
    rings.append(new_ring)
    if len(rings) > max_rings:
        rings.remove(rings[0])
    ring_hue += 10
    
layers = 3
layer_size = 30
def drawRings():
    global rings
    
    # noFill()
    for i, ring in enumerate(rings):
        # left ring
        if i%2 == 1:
            stroke(0)
            fill(ring[3]%100, 50, 100)
            ellipse(ring[0], ring[1], ring[2], ring[2])
            ring[2] += 1

        # right ring
        else:
            stroke(0)
            fill(ring[3]%100, 50, 100)
            ellipse(ring[0], ring[1], ring[2], ring[2])
            # ellipse(ring[0], ring[1], ring[2]+100*cos(PI/2*cur_angle), ring[2]+100*cos(PI/2*cur_angle))
            ring[2] += 1
            # for layer in xrange(layers):
            #     fill(ring[3]%100, 50-10*layer, 100)
            #     # stroke(cur_hue%100, 50, 100)
            #     ellipse(ring[0], ring[1], ring[2]-layer*layer_size, ring[2]-layer*layer_size)
            #     noStroke()
            #     ring[2] += 1
    
