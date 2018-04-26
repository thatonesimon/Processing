from config import *

# circle definitions
circles = []
num_circles = 25
max_rad = max(window_width, window_height) + 500
rad_step = max_rad/num_circles
radius = 100
angle = 0

start_color = Color(255,150,0)
end_color = Color(0, 255, 0)

def zooming_circles():
    global r, g, b, radius, angle
    
    zoom_setup()
    
    for c in circles:
        level_color = gradient(start_color, end_color, c.radius/float(max_rad))
        fill(level_color.r, level_color.g, level_color.b)
        # fill(level_color.r+sin(c.radius)*50, level_color.g+sin(c.radius)*50, level_color.b+sin(c.radius)*50)
        c.draw()
        c.radius += 1
        if(c.radius >= max_rad):
            # remove circle
            circles.remove(c)
            new_circle = Circle(centerX, centerY, 0)
            circles.append(new_circle)
    
    # r = 255*sin(angle)%255
    # for i in reversed(xrange(num_circles)):
    #     level_color = gradient(start_color, end_color, i/float(num_circles))
    #     fill(level_color.r, level_color.g, level_color.b)
    #     ellipse(centerX, centerY, (radius+rad_step*i)%1250, (radius+rad_step*i)%1250)
    # radius+=1
    # if radius > rad_step:
    #     radius = 0
    # angle+=0.01

setup = False
def zoom_setup():
    global setup
    if not setup:
        for i in xrange(num_circles):
            print i
            new_circle = Circle(centerX, centerY, max_rad - rad_step*i)
            circles.append(new_circle)
        setup = True
