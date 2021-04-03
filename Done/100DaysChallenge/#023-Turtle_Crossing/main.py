import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.colormode(255)
screen.title("Turtle Cross")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
cars_list = [CarManager() for car in range(20)]
p_turtle = Player()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    for car in cars_list:       
        if car.hit(p_turtle.pos()):
            game_is_on = False
            score.game_over()
            break
        car.move()
    screen.onkey(key='w', fun=p_turtle.move)
    if p_turtle.chck_finish():
        p_turtle.start_pos()
        score.update_level()
        for car in cars_list:
            car.add_speed()
            car.start_pos()
    
screen.exitonclick()