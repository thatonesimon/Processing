from config import *

num_blocks = 10
block_size = int(window_width / num_blocks)

def color_blocks(s, e):
    step = 0
    for i in xrange(num_blocks):
        c = s.gradient(e, i / (num_blocks - 1.0)).to_color()
        for row in xrange(int(window_width / num_blocks)):
            for column in xrange(int(window_height)):
                set(row + step, column, c)
        step += int(window_width / num_blocks)

blocks = []
offset = 0
grad_step = 1.0/num_blocks
grad_offset = grad_step
last_color = rand_color()
next_color = rand_color()
def moving_blocks():
    global offset, grad_offset, grad_step, last_color, next_color
    step = offset
    setup_moving_blocks()

    for b in blocks:
        draw_block(b)
        b.x -= 5
        if b.x+2*block_size <= 0:
            blocks.remove(b)
            last_block = blocks[len(blocks)-1]
            c = last_color.gradient(next_color, grad_offset).to_color()
            new_block = Block(last_block.x+block_size, 0, c)
            blocks.append(new_block)
            
            grad_offset += grad_step
            if grad_offset >= 1:
                grad_offset = grad_step
                last_color = next_color.cpy()
                next_color.randomize()

def draw_block(b):
    for x in xrange(block_size):
        for y in xrange(block_size):
            set(b.x+x+offset, b.y+y+centerY-block_size/2, b.color)

c_1 = rand_color()
c_2 = rand_color()
c_3 = rand_color()
setup = False
def setup_moving_blocks():
    global setup, last_color
    if not setup:
        x = 0
        for i in xrange(num_blocks):
            c = c_1.gradient(c_2, i / (num_blocks - 1.0)).to_color()
            b = Block(x, 0, c)
            blocks.append(b)
            x += block_size

        for i in xrange(1,num_blocks):
            c = c_2.gradient(c_3, i / (num_blocks - 1.0)).to_color()
            b = Block(x, 0, c)
            blocks.append(b)
            x += block_size
        last_color = c_3
        setup = True
