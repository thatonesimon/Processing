from config import *

add_library('minim')
player = None
beat = None
beat_size = 0

def setup():
    size(window_width, window_height, P2D)
    # fullScreen(P2D)
    colorMode(HSB, 100)
    background(100, 0, 100)
    # frameRate(1)
    global hand, head
    hand = loadImage("res/hand.png")
    head = loadImage("res/head.png")
    
    # music
    global minim, player, beat, beat_size
    minim = Minim(this)
    # aftergold, newshit, relax, song
    player = minim.loadFile("res/relax.mp3")
    beat = BeatDetect(player.bufferSize(), player.sampleRate())
    # prevent beat from hitting too often
    beat.setSensitivity(2000);
    player.play()
    beat_size = beat.detectSize() 
    
    global string_len
    string_len = height/2

def draw():
    global cur_hue
    translate(width/2, 0)
    background(100-cur_hue%100, 50, 100)
    
    # user inputted pulse
    pulseCheck()
    
    drawRings()
    onsetCheck()
    
    drawFlowers()
    drawHand()
    # drawHead()

    drawString()
    drawPen()
    
    cur_hue += 0.1
    
    # saveFrame("out/relax####.png")
    
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
        player.skip(-5000)
    # RIGHT
    elif keyCode == 39:
        player.skip(5000)
        
def drawHand():
    tint(cur_hue%100, 50, 100)
    image(hand, -140, 95)
    
def drawHead():
    tint(0, 0, 0)
    image(head, -100, 7*height/10, 200, 200*head.height/head.width)

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
weight = 2.65
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
last_spawn = 0
def addFlower():
    global flowers, flower_dir, test_flowers
    # play around with this flower color
    flower_color = Color(100-cur_hue%100, 50, 100)
    new_flower = Flower(string_start[0], string_start[1]+string_len, -PI/2, flower_color, flower_dir)
    flowers.append(new_flower)
    flower_dir *= -1
    # global last_spawn
    # time = millis()
    # print str(time-last_spawn)
    # last_spawn = time

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
    
    # noFill()
    for i, ring in enumerate(rings):
        # left ring
        if i%2 == 1:
            stroke(0)
            ring.draw(pulse)
            ring.radius += 1
            
            if ring.radius > 2*width:
                rings.remove(ring)

        # right ring
        else:
            stroke(0)
            ring.draw(pulse)
            ring.radius += 1
            
            if ring.radius > 2*width:
                rings.remove(ring)

   
pulse = 0
pulse_max = pen_size
def pulsate():
    global pulse
    pulse = pulse_max
    
def pulseCheck():
    global pulse
    
    beat.detect(player.mix)
        
    # if beat.isHat():
    #     print "hat"
    #     # pulsate()
    
    # if beat.isKick():
    #     print "kick"
    #     # pulsate()
        
    # if beat.isSnare():
    #     print "snare"
    #     # pulsate()
        
    # power of next note i guess
    # print player.right.level()
    if player.mix.level() > 0.45:
        pulsate()
    
        
    # 0.1 to stop calculations after a little
    if pulse > 0.1:
        pulse *= 0.9
        
onset_bubbles = []
def onsetCheck():
    global onset_bubbles
    for i in range(beat_size):
        if beat.isOnset(i):
            x = i*width/beat_size-width/2+beat_size/2
            new_circle = Circle(x, height, 10, cur_hue%100)
            onset_bubbles.append(new_circle)
            # print "onset: " + str(i)
    
    drawOnsetBubbles()
    
onset_swerve = 0.0
def drawOnsetBubbles():
    global onset_bubbles, onset_swerve
    
    for bubble in onset_bubbles:
        stroke(0, 0, 0, 0)
        bubble.draw(pulse/3.0)
        bubble.x += cos(onset_swerve)/2
        bubble.y -= 1.0
        if bubble.y <= 0.0-bubble.radius:
            onset_bubbles.remove(bubble)
            
    onset_swerve += 0.01
        
        
        
def stop():
    # always close Minim audio classes when you are finished with them
    player.close()
    # always stop Minim before exiting
    minim.stop()
