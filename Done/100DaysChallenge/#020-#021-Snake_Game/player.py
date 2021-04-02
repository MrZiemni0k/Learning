from turtle import Turtle
ALLIGMENT = "center"
FONT = ("Courier", 12, "bold")
class Player(Turtle):
    
    def __init__(self,height):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, height / 2 - 20)
        self.color("white")
        self.write(f"Score: {self.score}",font=FONT,align=ALLIGMENT)
        
    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",font=FONT,align=ALLIGMENT)
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over!\n"
                   f"Your score: {self.score}",font=FONT,align=ALLIGMENT)

        