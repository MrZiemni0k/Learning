from turtle import Turtle
from random import randint

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.shape('circle')
        self.color('brown','red')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.show_food(100,100)

    def show_food(self,width,height):
        
        x_cord = randint(width / -2 + 40, width / 2 - 40)
        x_cord -= abs(x_cord % 20) 
        y_cord = randint(height / -2 + 40, height / 2 - 40)
        y_cord -= abs(y_cord % 20) 
        self.goto(x_cord,y_cord)
        #print(f"({x_cord},{y_cord})")
    
        