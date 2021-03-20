def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_if_clear():
    if front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
    else:
        turn_left()

while not at_goal():
    move_if_clear()