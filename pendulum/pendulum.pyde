from config import *

add_library('minim')
player = None
beat = None

def setup():
    size(window_width, window_height)
    colorMode(HSB, 100)
    background(100, 0, 100)
    # frameRate(1)
    global hand, head
    hand = loadImage("res/hand.png")
    head = loadImage("res/head.png")
    
    # music
    global player, beat
    minim = Minim(this)
    player = minim.loadFile("res/relax.mp3")
    beat = BeatDetect(player.bufferSize(), player.sampleRate())
    # prevent beat from hitting too often
    beat.setSensitivity(300); 
    player.play()

def draw():
    global cur_hue
    translate(width/2, 0)
    background(100-cur_hue%100, 50, 100)
    
    # user inputted pulse
    pulseCheck()
    
    drawRings()
    drawFlowers()
    drawHand()
    drawHead()

    drawString()
    drawPen()
    
    cur_hue += 0.1
    
def mouseClicked():
    print mouseX
    print mouseY
    
def keyPressed():
    
    if key == " ":
        pulsate()
        
    elif key == "p":
        if player.isPlaying():
            player.pause()
        elif player.position() == player.length():
            player.rewind()
            player.play()
        else:
            player.play() 
        
    # UP
    elif keyCode == 38:
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
    image(hand, -140, 95)
    
def drawHead():
    tint(0, 0, 0)
    image(head, -100, 7*window_height/10, 200, 200*head.height/head.width)

string_len = 300
string_start = [0, 200]
string_end = [0, 0]
def drawString():
    global string_end
    
    # calculate string end 
    string_end[0] = string_start[0] + string_len*cos(cur_angle)
    string_end[1] = string_start[1] + string_len*sin(cur_angle)
    
    stroke(0)
    line(string_start[0], string_start[1], string_end[0], string_end[1])

pen_size = 50
cur_angle = PI/8
cur_hue = 0.0
direction = 1
gravity = PI/120/50
gravity_dir = 1
speed = 0.0
weight = 5.0
def drawPen():
    global cur_angle, direction, gravity, gravity_dir, speed
    
    fill(cur_hue%100, 50, 100)
    drawTail()
    stroke(0)
    ellipse(string_end[0], string_end[1], pen_size, pen_size)
    
    next_angle = cur_angle + speed
        
    # if reaching bottom from right to left <-
    if cur_angle < PI/2 and next_angle > PI/2:
        # print "Sweep right to left"
        gravity *= -1
        addFlower()

    # if reaching bottom from left to right ->
    elif cur_angle > PI/2 and next_angle < PI/2:
        # print "Sweep left to right"
        gravity *= -1
        addFlower()
        
    cur_angle = next_angle
    
    next_speed = speed+weight*gravity*gravity_dir
    
    # print degrees(cur_angle)
    # if reach left
    if speed >= 0 and next_speed < 0:
        addRing()
    
    # if reach right
    elif speed <= 0 and next_speed > 0:
        addRing()
        
    speed = next_speed
    
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
        
        
flowers = []
flower_size = 10
flower_dir = 1
num_petals = 5
flower_offset = -PI/2
def addFlower():
    global flowers, flower_dir, test_flowers
    # play around with this flower color
    flower_color = Color(100-cur_hue%100, 50, 100)
    new_flower = Flower(string_start[0], string_start[1]+string_len, -PI/2, flower_color, flower_dir)
    flowers.append(new_flower)
    flower_dir *= -1

flower_angle = 0
spiral_angle = 0
def drawFlowers():
    global flowers, spiral_angle
    
    for flower in flowers:
        # flower.draw(spiral_angle)
        flower.draw()
    # once flower has dissapeared, remove from array
    if len(flowers) > 0 and flowers[0].color.a <= 0:
        flowers.remove(flowers[0])
        
    spiral_angle += 0.01
    
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
    
    beat.detect(player.mix)
    if beat.isOnset():
        print "onset"
        pulsate()
        
    if beat.isHat():
        print "hat"
    
    if beat.isKick():
        print "kick"
        
    if beat.isSnare():
        print "snare"
    
    # print player.right.level()
    # if player.right.level() > 0.3:
    #     pulsate()
        
    # 0.1 to stop calculations after a little
    if pulse > 0.1:
        pulse *= 0.9
