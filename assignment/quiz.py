<<<<<<< HEAD
import random

def read_questions_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    questions = content.split('\n\n')
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
=======
>>>>>>> 2319ec5dec9c3b5649d3541f9753ad8f2aa9a73c

import random
import os
import tkinter as tk
from tkinter import messagebox

<<<<<<< HEAD
def run_quiz(questions):
    score = 0
    for i, question_data in enumerate(random.sample(questions, 10)):
        print(f"\nQuestion {i+1}:")
        correct, correct_text = ask_question(question_data)
        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_text}")
        print(f"Your current score is {score}/{i+1}")
        if input("Do you want to continue? (yes/no) ").strip().lower() != 'yes':
            break
    print(f"Your final score is {score}/{len(questions)}")
=======
class Quiz:
    def __init__(self, filename):
        self.filename = filename
        self.questions = self.read_questions_from_file()

    def read_questions_from_file(self):
        if not self.filename.endswith('.txt'):
            raise ValueError("Error: Only .txt files are supported.")
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"Error: The file '{self.filename}' does not exist.")
        
        with open(self.filename, 'r') as file:
            content = file.read()
        questions = content.split('\n\n')
        parsed_questions = []
        for question in questions:
            lines = question.strip().split('\n')
            if len(lines) < 6:
                continue  # Skip any improperly formatted questions
            question_text = lines[0]
            options = lines[1:5]
            correct_answer = lines[5].split(': ')[1].strip().lower()
            parsed_questions.append({
                'question': question_text,
                'options': options,
                'answer': correct_answer
            })
        return parsed_questions

class QuizApp:
    def __init__(self, root, quiz):
        self.root = root
        self.quiz = quiz
        self.score = 0
        self.current_question_index = 0
        self.questions = random.sample(self.quiz.questions, 10)
        
        self.root.title("Quiz Application")
        self.create_widgets()
        self.show_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=400, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.options = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.root, text="", variable=self.options, value=chr(97 + i), font=("Arial", 12))
            btn.pack(anchor='w', padx=20, pady=5)
            self.option_buttons.append(btn)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer, font=("Arial", 12), bg="blue", fg="white")
        self.submit_button.pack(pady=20)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.try_again_button = tk.Button(self.root, text="Try Again", command=self.try_again, font=("Arial", 12), bg="green", fg="white")
        self.try_again_button.pack(pady=20)
        self.try_again_button.pack_forget()  # Hide the try again button initially

    def show_question(self):
        question_data = self.questions[self.current_question_index]
        self.question_label.config(text=question_data['question'])
        self.options.set(None)
        for i, option in enumerate(question_data['options']):
            self.option_buttons[i].config(text=f"{chr(97 + i)}. {option}")

    def check_answer(self):
        selected_option = self.options.get()
        if not selected_option:
            messagebox.showwarning("Warning", "Please select an option.")
            return

        correct_option = self.questions[self.current_question_index]['answer']
        if selected_option == correct_option:
            self.score += 1

        self.score_label.config(text=f"Score: {self.score}")
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Your final score is {self.score}/10")
            self.submit_button.pack_forget()  # Hide the submit button
            self.try_again_button.pack()  # Show the try again button
>>>>>>> 2319ec5dec9c3b5649d3541f9753ad8f2aa9a73c

    def try_again(self):
        self.score = 0
        self.current_question_index = 0
        self.questions = random.sample(self.quiz.questions, 10)
        self.score_label.config(text="Score: 0")
        self.submit_button.pack(pady=20)
        self.try_again_button.pack_forget()
        self.show_question()

def start_quiz():
    file_path = 'quiz_question.txt'
    try:
        quiz = Quiz(file_path)
        root = tk.Tk()
        app = QuizApp(root, quiz)
        root.mainloop()
    except (FileNotFoundError, ValueError) as e:
        messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    start_quiz()
