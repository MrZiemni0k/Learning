import colors
import random
from turtle import Turtle as t
from turtle import Screen

jimmy = t()
jimmy.speed("fastest")
screen = Screen()
screen.colormode(255)
jimmy.penup()

def make_dot():
    jimmy.color(random.choice(colors.colors))
    jimmy.dot(20)

def make_row(xcord,ycord,amount,padx):
    x = xcord
    y = ycord
    for _ in range(amount):
        jimmy.setpos(x,y)
        make_dot()
        x += padx
_x = -200
_y = -200        
for row in range(10):
    make_row(_x,_y,10,40) 
    _y += 40   


screen.exitonclick()