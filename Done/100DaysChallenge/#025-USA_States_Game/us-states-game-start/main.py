from turtle import Turtle, Screen
from score import ScoreBoard
from answers import AnswerList
from turtle_answer import StateTurtle

_a = AnswerList()
screen = Screen()
screen.title("U.S.A States")
image = "./blank_states_img.gif"
screen.addshape(image)
usa_map = Turtle(shape=image)
_score = ScoreBoard()
game_on = True

while game_on:
    p_answer = screen.textinput(title="Guess the State",
                                prompt="Provide the State")
    
    if _a.check_list(p_answer):
        cords = _a.give_cords(p_answer)
        _state = StateTurtle(cords,p_answer)
        _score.update()
    elif p_answer.lower() == 'exit':
        _a.generate_csv()
        game_on = False
    else:
        _a.generate_csv()
        _score.game_over()
        game_on = False
    
    if _score.check_score():
        game_on = False
    


screen.exitonclick()