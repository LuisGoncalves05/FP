dict = {
    'down':(0,-1),
    'left':(-1,0),
    'up':(0,1),
    'right':(1,0)
    }

def find_treasure(pos, steps):
    if steps != []:
        next_x = pos[0] + dict[steps[0]][0]
        next_y = pos[1] + dict[steps[0]][1]
        pos = (next_x, next_y)
        return find_treasure (pos, steps[1:])
    else:
        return pos

