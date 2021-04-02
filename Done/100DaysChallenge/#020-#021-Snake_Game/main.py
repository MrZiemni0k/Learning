from turtle import Turtle, Screen
from time import sleep
from _snake import Snake
from food import Food
from player import Player
from board import Board

#20 x 20 (Pixels) - One Square
_width = 600
_height = 600
screen = Screen()
screen.setup(width=_width, height=_height)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
_s = Snake()
_f = Food()
_p = Player(_height)
_b = Board(_width, _height)
game_on = True
while game_on:
    screen.update()
    _s.move(screen)
    sleep(0.1)
    #print(_s.snake_body[0].pos())
    
    #Eat food - nom nom nom
    if _s.snake_body[0].distance(_f) < 10:
        _f.show_food(_width,_height)
        _s.add_body()
        _p.add_score()
    
    #Crash wall
    elif (abs(_s.snake_body[0].pos()[0]) >= (_width / 2 - 20) or
          abs(_s.snake_body[0].pos()[1]) >= (_height / 2 - 20)
        ):
        _p.game_over()
        game_on = False
    
    #Crashed into itself
    else:   
        for x in range(len(_s.snake_body)-1, 0, -1):
            if _s.snake_body[0].distance(_s.snake_body[x]) < 15:
                _p.game_over()
                game_on = False
    
screen.exitonclick()