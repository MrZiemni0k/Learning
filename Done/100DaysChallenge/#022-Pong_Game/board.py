from turtle import Turtle

class Board(Turtle):
    
    def __init__(self,width,height):
        super().__init__()
        self.width = width 
        self.height = height 
        self.penup()
        self.hideturtle()
        self.pencolor('white')       
        self.setheading(90)
        self.draw_center()
        self.draw_arc()
        self.draw_lines()

    
    def draw_center(self):
        self.pensize(5)
        self.setpos(0, self.height / -2 + 30)
        
        for _ in range(int((self.height - 80) / 40)):
            self.forward(20)
            self.pendown()
            self.forward(20)
            self.penup()

    def draw_lines(self):
        self.penup()
        self.setpos(self.width / -2 + 20, self.height / -2 + 40)
        self.pendown()
        
        for _ in range(2):
            self.pensize(1)
            self.color(40, 40, 40)
            self.forward(self.height - 80)
            self.right(90)
            self.pensize(5)
            self.color('white')
            self.forward(self.width - 40)
            self.right(90)
        self.penup()
            
    def draw_arc(self):
        self.color(52, 60, 79)
        self.pensize(3)
        self.setpos(self.width / -2 + 20, self.height / -2 + 40)
        self.setheading(0)
        self.pendown()
        self.circle(self.height / 2 - 40, 180)
        self.penup()
        self.setpos(self.width / 2 - 20, self.height / 2 - 40)
        self.setheading(180)
        self.pendown()
        self.circle(self.height / 2 - 40, 180)
        self.penup()
        self.setheading(90)