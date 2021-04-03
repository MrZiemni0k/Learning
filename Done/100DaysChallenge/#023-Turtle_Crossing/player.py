STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.fillcolor('green')
        self.shape('turtle')
        self.shapesize(stretch_wid=0.5)
        self.penup()
        self.setheading(90)
        self.start_pos()
    
    def start_pos(self):
        self.setpos(STARTING_POSITION)
    
    def move(self):
        self.forward(MOVE_DISTANCE)
    
    def chck_finish(self):
        if self.pos()[1] == FINISH_LINE_Y:
            return True
