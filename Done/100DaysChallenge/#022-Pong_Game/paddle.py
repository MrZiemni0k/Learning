from turtle import Turtle

MOVE_DISTANCE = 5

class Paddle(Turtle):
    
    def __init__(self, name, height, width, key_down, key_up):
        super().__init__()
        self.start = False
        self.name = name
        self.height = height
        self.penup()
        self.setpos(width, 0)
        self.color(150, 32, 47)
        self.shape('square')
        self.shapesize(stretch_len=5, stretch_wid=0.5)
        self.setheading(90)
        self.key_down = key_down
        self.key_up = key_up
        
    def move_up(self):
        self.start = True
        self.setheading(90)
    
    def move_down(self):
        self.start = True
        self.setheading(270)
        
    def move(self, screen): 
        
        if self.start:
            if self.pos()[1] == self.height / 2 - 90:
                screen.onkey(key=self.key_down, fun=self.move_down)
                if self.heading() == 270:
                    self.forward(MOVE_DISTANCE)   
            elif self.pos()[1] == self.height / -2 + 90:
                screen.onkey(key=self.key_up, fun=self.move_up)
                if self.heading() == 90:
                    self.forward(MOVE_DISTANCE)
            else:
                screen.onkey(key=self.key_up, fun=self.move_up)
                screen.onkey(key=self.key_down, fun=self.move_down)
                self.forward(MOVE_DISTANCE)
        else:
            screen.onkey(key=self.key_down, fun=self.move_down)
            screen.onkey(key=self.key_up, fun=self.move_up)