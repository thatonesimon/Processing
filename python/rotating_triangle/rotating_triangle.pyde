from config import *

def setup():

    size(720, 720, P2D)
    # size(720, 720, OPENGL)
    frameRate(30)



base_rot = 0
layer_scale = 8.0
layer_rot = 10.0
num_layers = 100
def draw():

    background(100)
    translate(width/2, height/2)
    rotate(radians(180))
    scale(width, height)

    global base_rot, layer_scale, layer_rot
    rotate(radians(base_rot))

    for layer in reversed(range(num_layers)):
        # fill(COLORS[layer%NUM_COLORS])
        beginShape()

        # for some reason, stroke seems to fill...
        stroke(COLORS[layer%NUM_COLORS])

        vertex(0, 1)
        vertex(cos(radians(30)), -sin(radians(30)))
        vertex(-cos(radians(30)), -sin(radians(30)))

        endShape(CLOSE)

        scale(layer_scale/10, layer_scale/10)
        rotate(radians(layer_rot))

        # scale(0.9, 0.9)
        # rotate(radians(1))

    # base_rot += 1
    # layer_scale = (layer_scale+0.05)%10
    layer_rot += 0.25
