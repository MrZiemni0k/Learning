from turtle import Turtle

ALLIGMENT = "center"
FONT = ("Courier", 10, "bold")

class StateTurtle(Turtle):
    
    def __init__(self,cords,text):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.hideturtle()
        self.goto(cords)  
        self.color("black")
        self.write(f'{text}',font=FONT,align=ALLIGMENT)            
        self.score = 0
        
        
