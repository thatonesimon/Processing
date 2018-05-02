from config import *

num_row = 20
num_col = 20
row_step = window_width/num_col
col_step = window_height/num_row

cells_taken = []
cur = [num_row/2,num_col/2]
dir = 0
#     0
#  3 cur 1
#     2
def generate_grid():
    global cur, dir
    setup_generate_grid()
    
    go = int(random(4))
    
    # if cur would just turn around
    if (go-2)%4 == dir:
        return
    
    if go == 0:
        # up
        next = [cur[0], cur[1]-1]
    elif go == 1:
        # right 
        next = [cur[0]+1, cur[1]]
    elif go == 2:
        # down
        next = [cur[0], cur[1]+1]
    elif go == 3:
        # left
        next = [cur[0]-1, cur[1]]
    
    # if next would move off the map
    if next[0] < 0 or next[0] >= num_row or next[1] < 0 or next[1] >= num_col:
        return
    
    if next in cells_taken:
        return
    
    cells_taken.append(cur)

    connect(next)
    cur = next
    dir = go
    saveFrame("img/grid-###.jpg")
    
def connect(next):
    
    stroke(255)
    line(cur[0]*col_step+col_step/2, cur[1]*row_step+row_step/2, next[0]*col_step+col_step/2, next[1]*row_step+row_step/2)
    
    
    
    
setup = False
def setup_generate_grid():
    global setup
    if not setup:
        setup = True
        
def reset_grid():
    global cur, cells_taken
    cur = [num_row/2,num_col/2]
    cells_taken = []
    background(0)
    
