from turtle import Turtle
import random
from time import sleep

BASIC_SPEED = 5

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color(126, 128, 17)    
        self.shape('circle')
        self.speed = BASIC_SPEED
        self.penup()
        self.bounce_amount = 0
        self.set_direction()
    
    def set_direction(self):
        self.xdirection = random.choice([1,-1])
        self.ydirection = random.choice([1,-1])
        
    def check_wall(self, height):
        
        wall_cord = height / 2 - 55
        x_cord = self.pos()[0]
        y_cord = self.pos()[1]
        if abs(y_cord + BASIC_SPEED) > wall_cord:
            left_speed = abs(wall_cord - y_cord) - BASIC_SPEED
            self.goto(x_cord + (BASIC_SPEED * self.xdirection),
                      wall_cord + (left_speed * self.ydirection))
            self.ydirection *= -1
            self.bounce_amount += 1
        else:
            self.ball_move()   
    
    def check_paddle(self, paddleleft, paddleright, height):
        
        x_cord = self.pos()[0]
        y_cord = self.pos()[1]
        if self.xdirection == 1:
            x_paddle = paddleright.pos()[0]
            y_paddle = paddleright.pos()[1]
        else:
            x_paddle = paddleleft.pos()[0]
            y_paddle = paddleleft.pos()[1]
        
        if abs(x_cord) > abs(x_paddle):
            self.ball_move()    
        elif abs(x_cord) + BASIC_SPEED > abs(x_paddle):
            if (y_cord < y_paddle + 50) and (y_cord > y_paddle - 50):
                left_speed = abs(x_paddle - x_cord) - BASIC_SPEED
                self.goto(x_paddle + (left_speed * self.xdirection),
                          y_cord + (BASIC_SPEED * self.ydirection))
                self.xdirection *= -1
                self.bounce_amount += 1
            else:
                self.ball_move()
        else:
            self.check_wall(height)

    
    def ball_move(self):
        
        x_cord = self.pos()[0]
        y_cord = self.pos()[1]
        self.goto(x_cord + (BASIC_SPEED * self.xdirection),
                  y_cord + (BASIC_SPEED * self.ydirection))
    
    def raise_speed(self):
        
        if self.bounce_amount == 5:
            self.speed += 2
            self.bounce_amount -= 5
    
    def check_winner(self, paddle):
        
        if abs(self.pos()[0]) > abs(paddle.pos()[0])+50:
            if self.pos()[0] < 0:
                self.speed = BASIC_SPEED
                return 1
            else:
                self.speed = BASIC_SPEED
                return 2
        return None
    
    def ball_restart(self):
        
        self.goto(0,0)
        self.set_direction()
        sleep(2)
        

        
        
        
