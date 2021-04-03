FONT = ("Courier", 24, "bold")

from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(-260, 250)
        self.color('white')
        self.lvl = 0
        self.update_level()

    def update_level(self):
        self.lvl += 1
        self.clear()
        self.write(f"Level: {self.lvl}", font=FONT)
    
    def game_over(self):        
        self.clear()
        self.setpos(0, 0)
        self.write(f"GAME OVER\nLevel: {self.lvl}", font=FONT, align='Center')
