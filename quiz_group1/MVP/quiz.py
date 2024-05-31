
import random
import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = random.sample(questions, 10)  
        self.score = 0
        self.current_question_index = 0

        self.question_label = tk.Label(master, wraplength=800, font=("Helvetica", 20))
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", command=lambda idx=i: self.answer_question(idx), font=("Helvetica", 16))
            button.pack(fill=tk.BOTH, padx=20, pady=10)
            self.option_buttons.append(button)

        self.status_label = tk.Label(master, text="", font=("Helvetica", 16))
        self.status_label.pack()

        self.quit_button = tk.Button(master, text="Quit", command=self.quit_quiz, font=("Helvetica", 16))
        self.quit_button.pack()

        self.try_again_button = tk.Button(master, text="Try Again", command=self.try_again, font=("Helvetica", 16))
        self.try_again_button.pack()
        self.try_again_button.pack_forget()        
        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data['question'])
            for i, option in enumerate(question_data['options']):
                self.option_buttons[i].config(text=option)
            self.status_label.config(text=f"Question {self.current_question_index + 1}/{len(self.questions)}")
        else:
            messagebox.showinfo("Quiz Finished", f"Your final score is {self.score}/{len(self.questions)}")
            self.try_again_button.pack()  

    def answer_question(self, selected_option):
        question_data = self.questions[self.current_question_index]
        correct_option_index = ord(question_data['answer']) - ord('a')
        if selected_option == correct_option_index:
            self.score += 1
        self.current_question_index += 1
        self.next_question()

    def quit_quiz(self):
        self.master.destroy()

    def try_again(self):
        self.master.destroy()
        main()

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

def main():
    file_path = 'quiz_question.txt'
    try:
        questions = read_questions_from_file(file_path)
        root = tk.Tk()
        root.title("Quiz App")
        root.attributes('-fullscreen', True) 
        app = QuizApp(root, questions)
        root.mainloop()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")

if __name__ == "__main__":
    main()
