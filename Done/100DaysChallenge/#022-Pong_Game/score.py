from turtle import Turtle
ALLIGMENT = "center"
FONT = ("Courier", 16, "bold")
WINS = 3

class Score(Turtle):
    
    def __init__(self, name, cords):
        super().__init__()
        self.name = name
        self.score = 0
        self.penup()
        self.setpos(cords)
        self.hideturtle()
        self.color("white")
        self.write(f"{self.name}: {self.score}",font=FONT,align=ALLIGMENT)
        
    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.name}: {self.score}",font=FONT,align=ALLIGMENT)
    
    def check_score(self):
        
        if self.score == WINS:
            self.clear()
            self.goto(0,0)
            self.write(f"{self.name} WINS!",font=FONT,align=ALLIGMENT)
            return True
        
        