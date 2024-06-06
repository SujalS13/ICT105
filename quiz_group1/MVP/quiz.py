import random
import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master, questions):
        # Initialize the quiz app with the given master window and questions
        self.master = master
        # Select 10 random questions from the given list of questions
        self.questions = random.sample(questions, 10)  
        # Initialize the score to 0
        self.score = 0
        # Initialize the current question index to 0
        self.current_question_index = 0

        # Create a label to display the current question
        self.question_label = tk.Label(master, wraplength=800, font=("Helvetica", 20), fg='red')
        self.question_label.pack()

        # Create 4 buttons to display the options for the current question
        self.option_buttons = []
        for i in range(4):
            # Create a button with a command that calls the answer_question method with the current option index
            button = tk.Button(master, text="", command=lambda idx=i: self.answer_question(idx), font=("Helvetica", 16), fg='blue', bg='black')
            button.pack(fill=tk.BOTH, padx=20, pady=10)
            self.option_buttons.append(button)

        # Create a label to display the current status (e.g. "Question 1/10")
        self.status_label = tk.Label(master, text="", font=("Helvetica", 16))
        self.status_label.pack()

        # Create a button to quit the quiz
        self.quit_button = tk.Button(master, text="Quit", command=self.quit_quiz, font=("Helvetica", 16))
        self.quit_button.pack()

        # Create a button to try again (hidden by default)
        self.try_again_button = tk.Button(master, text="Try Again", command=self.try_again, font=("Helvetica", 16))
        self.try_again_button.pack()
        self.try_again_button.pack_forget()     

        # Initialize the time left for each question to 30 seconds
        self.time_left = 30  
        # Create a label to display the time left
        self.timer_label = tk.Label(master, text=f"Time left: {self.time_left}s", font=("Helvetica", 16))
        self.timer_label.pack()
        # Start the timer
        self.update_timer()
   
        # Display the first question
        self.next_question()

    def next_question(self):
        # If there are more questions, display the next one
        if self.current_question_index < len(self.questions):
            # Get the current question data
            question_data = self.questions[self.current_question_index]
            # Display the question text
            self.question_label.config(text=question_data['question'])
            # Display the options
            for i, option in enumerate(question_data['options']):
                self.option_buttons[i].config(text=option)
            # Display the current status
            self.status_label.config(text=f"Question {self.current_question_index + 1}/{len(self.questions)}")
            # Reset the timer for each question
            self.time_left = 30  
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            # Start the timer
            self.update_timer()
        else:
            # If all questions have been answered, show the final score and hide the quiz
            messagebox.showinfo("Quiz Finished", f"Your final score is {self.score}/{len(self.questions)}")
            self.try_again_button.pack()  

    def answer_question(self, selected_option):
        # Get the current question data
        question_data = self.questions[self.current_question_index]
        # Get the correct answer index
        correct_option_index = ord(question_data['answer']) - ord('a')
        # Check if the user's answer is correct
        if selected_option == correct_option_index:
            # If correct, increment the score and show a success message
            self.score += 1
            self.show_answer_result(True)
        else:
            # If incorrect, show an error message
            self.show_answer_result(False)
        # Move to the next question
        self.current_question_index += 1
        self.next_question()
  
    def show_answer_result(self, is_correct):
        # Show a message box with the result of the user's answer
        if is_correct:
            messagebox.showinfo("Result", "Correct!")
        else:
            question_data = self.questions[self.current_question_index]
            correct_option_index = ord(question_data['answer']) - ord('a')
            correct_answer = question_data['options'][correct_option_index]
            messagebox.showinfo("Result", f"Incorrect! The correct answer is: {correct_answer}")

    def update_timer(self):
        # Decrement the time left and update the timer label
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}s
