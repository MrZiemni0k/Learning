from question_model import Question
from data import question_data
from quiz_brain import QuizCount

question_bank = []

for question in question_data:
    _text = question["text"]
    _answer = question["answer"]
    question_bank.append(Question(_text,_answer))
    
question_machine = QuizCount(question_bank)

while question_machine.still_has_questions():
    question_machine.next_question()
    
print("You've completed the quiz")
print(f"Your final score: {question_machine.score}/{question_machine.counter}")