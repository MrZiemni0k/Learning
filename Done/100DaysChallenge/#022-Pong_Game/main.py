from turtle import Turtle, Screen
from paddle import Paddle
from time import sleep
from board import Board
from ball import Ball
from score import Score

_WIDTH = 1200
_HEIGHT = 600
screen = Screen()
screen.colormode(255)
screen.title("Pong")
screen.listen()
screen.tracer(0)
screen.setup(width=_WIDTH, height=_HEIGHT)
screen.bgcolor('black')

_scorep1 = Score(name='Player1', cords=(_WIDTH / -4 + 20, _HEIGHT / 2 - 30))
_scorep2 = Score(name='Player2', cords=(_WIDTH / 4 - 20, _HEIGHT / 2 - 30))
_b = Board(width=_WIDTH, height=_HEIGHT)
_ball =Ball()
_p1 = Paddle(name='Player1',
             height=_HEIGHT,
             width=_WIDTH / -2 + 20,
             key_down='s',
             key_up='w')
_p2 = Paddle(name='Player2',
             height=_HEIGHT,
             width=_WIDTH / 2 - 20,
             key_down='Down',
             key_up='Up')

game_on = True
while game_on:
    screen.update()
    sleep(0.01)
    _p1.move(screen)
    _p2.move(screen)
    _ball.check_paddle(_p1,_p2,_HEIGHT)
    _ball.raise_speed()
    if _ball.check_winner(_p1) == 1:
        _scorep2.add_score()
        _ball.ball_restart()
        screen.update()
    elif _ball.check_winner(_p2) == 2:
        _scorep1.add_score()
        _ball.ball_restart()
        screen.update()
    if _scorep1.check_score():
        _scorep2.clear()
        break
    elif _scorep2.check_score():
        _scorep1.clear()
        break
    
screen.exitonclick()