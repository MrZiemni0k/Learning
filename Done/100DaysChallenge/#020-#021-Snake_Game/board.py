from turtle import Turtle

class Board(Turtle):
    
    def __init__(self, width, height):
        super().__init__()      
        self.left(90)
        self.width = width
        self.height = height
        self.fillcolor(18, 28, 21)
        self.penup()
        self.goto(width / -2 + 20, height / -2 + 20)
        self.pendown()
        self.hideturtle()
        self.draw_board()
        
    def draw_board(self):
        
        self.begin_fill()
        for _ in range(2):
            self.forward(self.height - 40)
            self.right(90)
            self.forward(self.width - 40)
            self.right(90)
        self.end_fill()
        