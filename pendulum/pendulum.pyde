from config import *

def setup():
    size(window_width, window_height)
    colorMode(HSB, 100)
    background(100, 0, 100)
    # frameRate(1)
    global hand, head
    hand = loadImage("res/hand.png")
    head = loadImage("res/head.png")

it = 0
def draw():
    global string_end, cur_angle, cur_hue, direction, gravity, gravity_dir, speed
    
    global it
    it += 1
    print it
    
    # user inputted pulse
    pulseCheck()
    
    background(100-cur_hue%100, 50, 100)
    drawRings()
    drawBubbles()
    drawHand()
    drawHead()
    
    # calculate string end 
    string_end[0] = string_start[0] + string_len*cos(cur_angle)
    string_end[1] = string_start[1] + string_len*sin(cur_angle)

    drawString()
    drawPen()
    
    next_angle = cur_angle + speed

    # if passing by bottom of swing leftwards
    if next_angle > PI/2 and cur_angle < PI/2:
        print PI/2-next_angle
        print PI/2-cur_angle
        addBubble()
    
    # if passing by bottom of swing rightwards
    elif next_angle < PI/2 and cur_angle > PI/2:
        addBubble()
        
    # if reaching bottom from right to left <-
    if cur_angle < PI/2 and next_angle > PI/2:
        # print "Sweep right to left"
        gravity *= -1

    # if reaching bottom from left to right ->
    elif cur_angle > PI/2 and next_angle < PI/2:
        # print "Sweep left to right"
        gravity *= -1
    
    cur_angle = next_angle
    
    next_speed = speed+weight*gravity*gravity_dir
    # print degrees(cur_angle)
    if speed >= 0 and next_speed < 0:
        print "Hit left " + str(PI/2-cur_angle)
        addRing()
    elif speed <= 0 and next_speed > 0:
        print "Hit right " + str(PI/2-cur_angle)
        addRing()
    speed = next_speed
    
    cur_hue += 0.1
    
def mouseClicked():
    print mouseX
    print mouseY
    
def keyPressed():
    
    if key == " ":
        pulsate()
        
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
    tint(0, 0, 0)
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
gravity = PI/120/50
gravity_dir = 1
speed = 0.0
weight = 10.0
def drawPen():
    fill(cur_hue%100, 50, 100)
    drawTail()
    stroke(0)
    ellipse(string_end[0], string_end[1], pen_size, pen_size)
    
num_trails = 4
def drawTail():
    # noStroke()
    for i in reversed(xrange(num_trails)):
        stroke(0, 0, 0, 100-100*i/num_trails)
        fill(cur_hue%100, 50, 100, 100-100*i/num_trails)
        tail_center = [None, None]
        tail_center[0] = string_start[0] + string_len*cos(cur_angle-i*speed)
        tail_center[1] = string_start[1] + string_len*sin(cur_angle-i*speed)
        ellipse(tail_center[0], tail_center[1], pen_size-5*i, pen_size-5*i)
        # ellipse(tail_center[0], tail_center[1], pen_size-5*i, pen_size)
        
        
bubbles = []
bubble_size = 10
bubble_dir = 0
def addBubble():
    global bubbles, bubble_dir
    bubble_group = []
    for i in xrange(4):
        bubble = Circle(string_start[0], string_start[1]+string_len, bubble_size, 100-cur_hue%100)
        bubble_group.append(bubble)
    bubbles.append([bubble_group, bubble_dir%2])
    bubble_dir += 1
    
bubble_angle = 0
def drawBubbles():
    global bubbles
    
    for i, bubble_group in enumerate(bubbles):
        if bubble_group[1] == 0:
            bubble_angle = 0
        else:
            bubble_angle = PI/4
        for i, bubble in enumerate(bubble_group[0]):
            bubble.draw()
            direction = i%4
            # right
            if direction == 0:
                bubble.x += cos(bubble_angle)
                bubble.y += sin(bubble_angle)
            # down
            elif direction == 1:
                bubble.x -= sin(bubble_angle)
                bubble.y += cos(bubble_angle)
            # left
            elif direction == 2:
                bubble.x -= cos(bubble_angle)
                bubble.y -= sin(bubble_angle)
            # up
            elif direction == 3:
                bubble.x += sin(bubble_angle)
                bubble.y -= cos(bubble_angle)
        
            bubble.color.a -= 0.5
            
        # once bubble has dissapeared, remove from array
        if bubble_group[0][0].color.a == 0:
            bubbles.remove(bubble_group)
    
rings = []
ring_hue = 0.0
max_rings = 15
def addRing():
    global rings, ring_hue
    new_ring = Circle(string_end[0], string_end[1], 0, 100-cur_hue%100)
    rings.append(new_ring)
    # if len(rings) > max_rings:
    #     rings.remove(rings[0])
    ring_hue += 10
    
layers = 3
layer_size = 30
# TODO: change ring size on algorithm
def drawRings():
    global rings
    
    # noFill()
    for i, ring in enumerate(rings):
        # left ring
        if i%2 == 1:
            stroke(0)
            ring.draw(pulse)
            ring.radius += 1
            
            if ring.radius > width:
                rings.remove(ring)

        # right ring
        else:
            stroke(0)
            ring.draw(pulse)
            ring.radius += 1
            
            if ring.radius > width:
                rings.remove(ring)
            # for layer in xrange(layers):
            #     fill(ring[3]%100, 50-10*layer, 100)
            #     # stroke(cur_hue%100, 50, 100)
            #     ellipse(ring[0], ring[1], ring[2]-layer*layer_size, ring[2]-layer*layer_size)
            #     noStroke()
            #     ring[2] += 1
   
pulse = 0
pulse_max = pen_size
def pulsate():
    global pulse
    pulse = pulse_max
    
def pulseCheck():
    global pulse
    # 0.1 to stop calculations after a little
    if pulse > 0.1:
        pulse *= 0.9
