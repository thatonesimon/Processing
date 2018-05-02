from config import *

string_len = 400
string_start = [centerX, 200]
string_end = [0, 0]
pen_size = 50

cur_angle = PI/4
cur_hue = 0.0

direction = 1
gravity = 0.001
gravity_dir = 1
speed = 0.0


def setup():
    size(window_width, window_height)
    colorMode(HSB, 100)
    background(100, 0, 100)
    # frameRate(1)
    
    global img
    img = loadImage("res/hand.jpeg")
    
def draw():
    global string_end, cur_angle, cur_hue, direction, gravity, gravity_dir, speed
    
    background(100-cur_hue%100, 50, 100)
    image(img,centerX, centerY)
    
    string_end[0] = string_start[0] + string_len*cos(cur_angle)
    string_end[1] = string_start[1] + string_len*sin(cur_angle)
    
    stroke(0)
    # stroke(cur_hue%100, 75, 100)
    fill(cur_hue%100, 50, 100)
    line(string_start[0], string_start[1], string_end[0], string_end[1])
    # stroke(cur_hue%100, 75, 100)
    ellipse(string_end[0], string_end[1], pen_size, pen_size)
    
    next_angle = cur_angle + speed

    # # if passing by bottom of swing leftwards
    # if next_angle - cur_angle > 0 and cur_angle > PI/2:
    #     gravity_dir = -1
    
    # # if passing by bottom of swing rightwards
    # elif next_angle - cur_angle < 0 and cur_angle < PI/2:
    #     gravity_dir = -1
        
    # if reach max left or right
    # TODO: count only the max hit
    if cur_angle < PI/4:
        print "Hit right"
    if cur_angle > 3*PI/4:
        print "Hit left"
        
    # if reaching bottom from right to left <-
    if cur_angle < PI/2 and next_angle > PI/2:
        print "Sweep right to left"
        gravity *= -1
    # if reaching bottom from left to right ->
    if cur_angle > PI/2 and next_angle < PI/2:
        print "Sweep left to right"
        gravity *= -1
    
    cur_angle = next_angle
    speed += gravity*gravity_dir
    print degrees(cur_angle)
    
    cur_hue += 0.1
    
