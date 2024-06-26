import random
import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master, questions):
        # Initialize the quiz app with a master window and a list of questions
        self.master = master
        self.questions = random.sample(questions, 10)  # Select 10 random questions from the list
        self.score = 0
        self.current_question_index = 0

        # Create the question label
        self.question_label = tk.Label(master, wraplength=800, font=("Helvetica", 20))
        self.question_label.pack()

        # Create the option buttons
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", command=lambda idx=i: self.answer_question(idx), font=("Helvetica", 16))
            button.pack(fill=tk.BOTH, padx=20, pady=10)
            self.option_buttons.append(button)

        # Create the status label
        self.status_label = tk.Label(master, text="", font=("Helvetica", 16))
        self.status_label.pack()

        # Create the quit button
        self.quit_button = tk.Button(master, text="Quit", command=self.quit_quiz, font=("Helvetica", 16))
        self.quit_button.pack()

        # Create the try again button
        self.try_again_button = tk.Button(master, text="Try Again", command=self.try_again, font=("Helvetica", 16))
        self.try_again_button.pack()
        self.try_again_button.pack_forget()  # Hide the try again button initially

        # Initialize the timer
        self.time_left = 30  # 30 seconds for each question
        self.timer_label = tk.Label(master, text=f"Time left: {self.time_left}s", font=("Helvetica", 16))
        self.timer_label.pack()
        self.update_timer()  # Start the timer

        # Start the quiz with the first question
        self.next_question()

    def next_question(self):
        # Display the next question
        if self.current_question_index < len(self.questions):
            # Get the current question data
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data['question'])  # Set the question text
            for i, option in enumerate(question_data['options']):
                self.option_buttons[i].config(text=option)  # Set the option text
            self.status_label.config(text=f"Question {self.current_question_index + 1}/{len(self.questions)}")
            self.time_left = 30  # Reset the timer for each question
            self.timer_label.config(text=f"Time left: {self.time_left}s")
        else:
            # If no more questions, show the final score and enable the try again button
            messagebox.showinfo("Quiz Finished", f"Your final score is {self.score}/{len(self.questions)}")
            self.try_again_button.pack()

    def answer_question(self, selected_option):
        # Check if the user's answer is correct
        question_data = self.questions[self.current_question_index]
        correct_option_index = ord(question_data['answer']) - ord('a')  # Convert 'a'-'d' to 0-3
        if selected_option == correct_option_index:
            self.score += 1  # Increment score if correct
            self.show_answer_result(True)
        else:
            self.show_answer_result(False)

    def show_answer_result(self, is_correct):
        # Show the result of the user's answer
        if is_correct:
            messagebox.showinfo("Result", "Correct!")
        else:
            question_data = self.questions[self.current_question_index]
            correct_option_index = ord(question_data['answer']) - ord('a')
            correct_answer = question_data['options'][correct_option_index]
            messagebox.showinfo("Result", f"Incorrect! The correct answer is: {correct_answer}")
        self.current_question_index += 1  # Move to the next question
        self.next_question()

    def update_timer(self):
        # Update the timer every second
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.master.after(1000, self.update_timer)
        else:
            # Time's up! Show the result and move to the next question
            self.show_answer_result(False)
            self.update_timer()

    def quit_quiz(self):
        # Quit the quiz and close the window
        self.master.destroy()

    def try_again(self):
        # Restart the quiz
        self.master.destroy()
        self.update_timer()
        main()

def read_questions_from_file(filename):
    # Read the questions from a file
    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFOundError:
        messagebox.showerror("Error",f"File{filename} not found.")
        return []
    questions = content.strip().split('\n\n')
    parsed_questions = []
    for question in questions:
        lines = question.strip().split('\n')
        question_text = lines[0]
        options = lines[1:5]
        correct_answer = lines[5].split(': ')[1].strip().lower()
        parsed_questions.append({
            'question': question_text,
            'options': options,
            'answer': correct_answer
        })
    return parsed_questions

def main():
    # Main function to start the quiz application
    questions = read_questions_from_file('quiz_question.txt')
    root = tk.Tk()
    root.attributes('-fullscreen', True)  # Set the window to full screen
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))  # Bind the Escape key to exit full screen
    app = QuizApp(root, questions)
    root.mainloop()

if __name__ == "__main__":
    main()
