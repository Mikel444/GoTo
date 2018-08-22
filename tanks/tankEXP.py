def make_choice(x,y,field):
    width = len(field)
    height = len(field[0])
    left()

def left(x,y,field):
    for i in range(0, x):
        if field[i][y] == 1:
            return "go_left"

    for i in range(0, x):
        if field[i][y] not in [-1, 0 ,1]: 
            return "fire_left"
    right()

def right(x,y,field):
    for i in range(0, x):
        if field[i][y] == 1:
            return "go_right"

    for i in range(0, x):
        if field[i][y] not in [-1, 0 ,1]: 
            return "fire_right"
    up()

def up(x,y,field):
    for i in range(y, 0):
        if field[i][y] == 1:
            return "go_up"

    for i in range(y, 0):
        if field[i][y] not in [-1, 0 ,1]: 
            return "fire_up"
    down()

def down(x,y,field):
    for i in range(y, 0):
        if field[i][y] == 1:
            return "go_down"

    for i in range(y, 0):
        if field[i][y] not in [-1, 0 ,1]: 
            return "fire_down"
    make_choise()

make_choise()

