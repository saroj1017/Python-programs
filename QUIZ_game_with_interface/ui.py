from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=500, height=450)
        self.display_text = self.canvas.create_text(250, 226,
                                                    width=480,
                                                    text="some quiz text here making ir very nig",
                                                    font=("Ariel", 20, "italic"))
        self.canvas.grid(padx=40, row=1, column=0, columnspan=2)

        self.score_label = Label(text="Score : 0", bg=THEME_COLOR, fg="white", font=("Ariel", 15, "bold"))
        self.score_label.config(padx=30, pady=30)
        self.score_label.grid(row=0, column=1)

        # self.true_button = Button(text="images/false.png")
        #
        img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=img, borderwidth=0, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(pady=30, row=2, column=0)

        img2 = PhotoImage(file="images/false.png")
        self.false_button = Button(image=img2, borderwidth=0, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(pady=30, row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        # self.window.after_cancel(1000)
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.display_text, text=q_text)
        else:
            self.canvas.itemconfig(self.display_text, text="you have reached end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

        # if self.quiz.check_answer("True"):
        #     self.canvas.config(bg="green")
        # else:
        #     self.canvas.config(bg="red")
        # self.window.after(1000, self.get_next_question)

    def false_pressed(self):

        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

        # if self.quiz.check_answer("False"):
        #     self.canvas.config(bg="green")
        # else:
        #     self.canvas.config(bg="red")
        # self.window.after(1000, self.get_next_question)
        #
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



