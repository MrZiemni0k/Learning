class QuizCount:
    
    def __init__(self, q_list):
        self.counter = 0
        self.q_list = q_list
        self.score = 0
        
    def next_question(self):
        current_question = self.q_list[self.counter]
        self.counter += 1
        user_answer = input(f"Q.{self.counter}: {current_question.text} \n"
                            "True/False\n")
        self.check_answer(user_answer, current_question.answer)
    
    def still_has_questions(self):
        return self.counter < len(self.q_list)
    
    def check_answer(self, u_answer, q_answer):
        if u_answer[0].lower() == q_answer[0].lower():
            print("That's correct!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"Correct answer was: {q_answer.upper()}")
        print(f"Your score is: {self.score}/{self.counter}")
        print("\n")

            