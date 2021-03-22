counter = 0

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_if_clear():
    global counter
    if front_is_clear():
        if right_is_clear():
            if counter > 3:
                move()                
                counter = 0
            else:
                turn_right()
                move()
                counter += 1
        else:
            move()
            counter = 0
    elif right_is_clear():
        turn_right()
        move()
    else:
        turn_left()

while not at_goal():
    move_if_clear()