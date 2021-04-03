COLORS = ["red", "orange", "yellow", "pink", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
from turtle import Turtle

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self._speed = STARTING_MOVE_DISTANCE
        self.color(COLORS[random.randint(0,len(COLORS)-1)])
        self.penup()
        self.setheading(180)
        self.start_pos()
    
    def start_pos(self):
        self.setpos(random.randrange(-300, 300, 20),
                    random.randrange(-260, 260, 20))
        
    def move(self):
        self.refresh()
        self.forward(self._speed)
        
    def refresh(self):
        if self.pos()[0] < -320:
            self.setpos(320, random.randrange(-260, 260, 20))
    
    def add_speed(self):
        self._speed += MOVE_INCREMENT
        
    def hit(self, turtle_pos):        
        if turtle_pos[1] == self.pos()[1]:
            if self.pos()[0] - 25 <= turtle_pos[0] <= self.pos()[0] + 25:
                return True