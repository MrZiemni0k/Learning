from turtle import Turtle, Screen
import random

_width = 500
_height = 500
screen = Screen()
screen.setup(width=_width, height=_height)

#Turtles
_r = Turtle(shape="turtle")
_r.color('red')
_r.speed('fastest')
_g = Turtle(shape="turtle")
_g.color =('black')
_g.speed('fastest')
_b = Turtle(shape="turtle")
_b.color('blue')
_b.speed('fastest')
_p = Turtle(shape="turtle")
_p.color('pink')
_p.speed('fastest')
_y = Turtle(shape="turtle")
_y.color('yellow')
_y.speed('fastest')

turtle_list = [_r, _g, _b, _p, _y]


screen.setup(width=500, height=400)

def turtle_startpos():
    y = _height/4-_height/2
    for x in turtle_list:
        x.penup()
        x.setposition((10-_width/2, y))
        y += _height / 8
        
def random_move():
    
    for x in turtle_list:
        x.forward(random.randint(0,5))

def check_winner():
    
    x_cords = []
    x0 = []
    for x in turtle_list:
        if x.pos()[0] >= (_width / 2)-22:
            x_cords.append(x)
            x0.append(x.pencolor()[0])
            
    if x_cords:
        print("The winners are: ")
        for x in x_cords:
            print(x.color()[0])
        
        print(f"Your bet was: {user_bet}")
            
        if  user_bet.lower()[0] in x0:
            print("You won!")
            return False
        else:
            print("You lost")
            return False
    return True   
         
turtle_startpos()
user_bet = screen.textinput(title="Make your bet",
                            prompt=("Which turtle will win the race?\n"
                                   "Choose colour.\n"
                                   "Red / Black / Blue / Pink / Yellow")
                            )

while check_winner():
    random_move()
  
screen.exitonclick()