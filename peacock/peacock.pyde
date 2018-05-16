from config import *

def setup():
    size(720, 720, P2D)
    
    
num_layers = 10
max_layer_len = 50
layer_len = max_layer_len
num_feathers = 10
base_angle = 0

growth_direction = 1
def draw():
    background(0)
    translate(width/2, height/2)
    # scale(0.25, 0.25)
    
    global base_angle, layer_len, growth_direction
    rotate(radians(base_angle))
    for layer in range(num_layers):
        rotate(radians(360/(num_feathers*num_layers)))
        for i in range(num_feathers):
            rotate(radians(360/num_feathers))
            feather = Feather((layer+1)*layer_len, 5+(layer+1)/2)
            feather.show()
        
    
    base_angle -= 0.5
    layer_len = max_layer_len*sin(radians(base_angle))
    
    # if layer_len > max_layer_len or layer_len < 0:
    #     growth_direction *= -1
    
    # saveFrame("./out/peacock##.jpg")
    
    
