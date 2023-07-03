from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_brain import QuizBrain
import tkinter as tk
from PIL import Image, ImageTk

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):

        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("Quiz Application")
        self.window.geometry("850x530")
        self.window.configure(bg="#F6F1E9")
        #display title
        self.display_title()
        #canvas for question text and display question
        
        self.canvas=Canvas(width=800,height=250)
        self.question_text=self.canvas.create_text(400,125,text="Question",width=680,fill="#03001C",font=('Ariel',15,'italic'))
        self.canvas.grid(row=2,column=0,columnspan=2,pady=50)
        self.canvas.configure(background='#F6F1E9')
        self.display_question()
        #StringVar to store user's answer
        self.user_answer=StringVar()
        #Display four options radio buttons
        self.opts=self.radio_buttons()
        self.display_options()
        #Submit button to check if an option is selected or not before submitting answers
        #submit_btn= Button(text ="submit",command=lambda : self.check_selected())
        #to show whether answer right or wrong
        self.feedback=Label(self.window,pady=10, bg="#F6F1E9",font=("ariel",15,"bold"))
        self.feedback.place(x=300,y=380)
        #Next and Quit button
        self.buttons()
        #mainloop
        developed_label = tk.Label(self.window, text="Developed By Rakesh",  bg="#F6F1E9",fg="gray",font=("ariel",10,"bold"))
        developed_label.place(x=20,y=40)
     
        self.window.mainloop()


    def display_title(self):
        title=Label(self.window,text= " Quiz Application ",width=50,bg="red",fg="white",font=("ariel",20,"bold"))
        #place of title
        title.place(x=0,y=2) 

    def display_question(self):
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)

    def radio_buttons(self):
        #create four options
        choice_list=[]
        y_pos=220
        while len(choice_list)<4:
            #setting radio button properties
            radio_btn=Radiobutton(self.window,text="",variable=self.user_answer, bg="#F6F1E9",value="",font=("ariel",14,"bold"))
            #adding the button to the list
            choice_list.append(radio_btn)   
            #place the button
            radio_btn.place(x=200,y=y_pos)
            y_pos +=40

        return choice_list

    def display_options(self):
        """To display four options"""

        val = 0

        # deselecting the options
        self.user_answer.set(None)

        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):
        """To show feedback for each answer and keep checking for more questions"""

        # Check if the answer is correct
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Correct answer! \U0001F44D'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('\u274E Oops! \n'
                                     f'The right answer is: {self.quiz.current_question.correct_answer}')

        if self.quiz.has_more_questions():
            # Moves to next to display next question and its options
            self.display_question()
            self.display_options()
        else:
            # if no more questions, then it displays the score
            self.display_result()


    def buttons(self):
        """To show next button and quit button"""

        # The first button is the Next button to move to the
        # next Question
        next_button = Button(self.window, text="Next", command=self.next_btn,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))

        # palcing the button on the screen
        next_button.place(x=350, y=460)

        # This is the second button which is used to Quit the self.window
        quit_button = Button(self.window, text="Quit", command=self.window.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))

        # placing the Quit button on the screen
        quit_button.place(x=700, y=50)
    def display_result(self):
     self.window.destroy()
     ans_window = tk.Tk()
     ans_window.title("Quiz Application")
     ans_window.geometry("850x530")
     ans_window.configure(bg="#F6F1E9")  # Set the background color

     title1 = Label(ans_window, text="Quiz Application", width=50, bg="red", fg="white", font=("Arial", 20, "bold"))
     title1.grid(row=0, column=0, columnspan=2)

     developed_label = tk.Label(ans_window, text="Developed By Rakesh", fg="gray", font=("Arial", 10, "bold"), bg="#F6F1E9")
     developed_label.grid(row=1, column=0, sticky="w", padx=20, pady=10)

     correct, wrong, score_percent = self.quiz.get_score()
     result = f"Score: {score_percent}%"
     correct = f"Correct: {correct}"
     wrong = f"Wrong: {wrong}"

     result_label = tk.Label(ans_window, text=result, bg="#F6F1E9", font=("Arial", 16, "bold"))
     result_label.grid(row=2, column=0, columnspan=2, pady=10)

     correct_label = tk.Label(ans_window, text=correct, bg="#F6F1E9", font=("Arial", 16, "bold"))
     correct_label.grid(row=3, column=0,columnspan=2, pady=10)

     wrong_label = tk.Label(ans_window, text=wrong, bg="#F6F1E9", font=("Arial", 16, "bold"))
     wrong_label.grid(row=4, column=0,columnspan=2, pady=10)

     exit_button = Button(ans_window, text="Exit", command=ans_window.destroy,
                         width=5, bg="green", fg="white", font=("Arial", 16, "bold"))
     exit_button.place(x=700, y=50)

     ans_window.mainloop()

   