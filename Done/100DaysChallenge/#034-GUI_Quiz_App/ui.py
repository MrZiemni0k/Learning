import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 16, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = tk.Label(text=f'Score: {self.quiz.score}',
                                    bg=THEME_COLOR,
                                    fg='white')
        self.label_score.grid(row=0, column=1)

        self.canvas = tk.Canvas(height=250, width=300, bg='white', bd=0)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(
                150, 125,
                width=280,
                text='test',
                font=FONT,
                fill=THEME_COLOR
        )

        image_true = tk.PhotoImage(file='./images/true.png')
        image_false = tk.PhotoImage(file='./images/false.png')
        self.btn_true = tk.Button(
                image=image_true,
                highlightthickness=0,
                bd=0,
                command=lambda: self.check_answer(answer='True'),
                padx=20, pady=20
        )
        self.btn_true.grid(row=2, column=0)
        self.btn_false = tk.Button(
                image=image_false,
                highlightthickness=0,
                bd=0,
                command=lambda: self.check_answer(answer='False'),
                padx=20, pady=20
        )
        self.btn_false.grid(row=2, column=1)

        self.new_question()

        self.window.mainloop()

    def new_question(self):
        self.canvas.configure(bg='white')
        self.label_score.config(text=f'Score: {self.quiz.score}')
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text,
                                   text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text,
                                   text='You\'ve reached the end of the quiz.')
            self.btn_false.config(state='disabled')
            self.btn_true.config(state='disabled')

    def check_answer(self, answer: str) -> None:
        self.give_feedback(self.quiz.check_answer(answer))

    def give_feedback(self, is_right: bool) -> None:
        if is_right:
            self.canvas.configure(bg='green')
            self.window.after(1000, self.new_question)
        else:
            self.canvas.configure(bg='red')
            self.window.after(1000, self.new_question)
