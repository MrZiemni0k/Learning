from turtle import Turtle

ALLIGMENT = "center"
FONT = ("Courier", 16, "bold")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(200,250)       
        self.color("black")
        self.score = 0
        self.write(f'{self.score}/50',font=FONT,align=ALLIGMENT)
        
        
    def update(self):
        self.clear()
        self.score += 1
        self.write(f'{self.score}/50',font=FONT,align=ALLIGMENT)
        
    def check_score(self):
        
        if self.score == 50:
            self.clear()
            self.goto(0,0)
            self.write(f"You got them all correct!",font=FONT,align=ALLIGMENT)
            return True
    
    def game_over(self):

        self.clear()
        self.goto(0,0)
        self.write(f"Game Over! You got {self.score} out of 50 correct.",font=FONT,align=ALLIGMENT)