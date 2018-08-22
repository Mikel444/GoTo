import random

actions = ['go_up','go_down','go_left','go_right']
x_line = ["go_right","go_left"]
y_line = ["go_up","go_down"]


def make_choice(x,y,field):
    width = len(field)
    height = len(field[0])

##left
    for i in range(x-1, -1, -1):
        if field[i][y] == 1:
            return "go_left"
        if field[i][y] == -1:
            break
        if field[i][y] not in [-1, 0 ,1]:
            if field[i][y]['life'] > field[x][y]['life']:
                return random.choice(y_line)
            else:
                return "fire_left"


##right
    for i in range(x+1, width):
        if field[i][y] == 1:
            return "go_right"
        if field[i][y] == -1:
            break
        if field[i][y] not in [-1, 0 ,1]: 
            if field[i][y]['life'] > field[x][y]['life']:
                return random.choice(y_line)
            else:
                return "fire_right"
            
##up
    for i in range(y-1,-1,-1):
        if field[x][i] == 1:
            return "go_up"
        if field[x][i] == -1:
            break
        if field[x][i] not in [-1, 0 ,1]: 
            if field[x][i]['life'] > field[x][y]['life']:
                return random.choice(x_line)
            else:
                return "fire_up"


##down
    for i in range(y+1, height):
        if field[x][i] == 1:
            return "go_down"
        if field[x][i] == -1:
            break
        if field[x][i] not in [-1, 0 ,1]:
            if field[x][i]['life'] > field[x][y]['life']:
                return random.choice(x_line)
            else:
                 return "fire_down"

    return random.choice(actions)
