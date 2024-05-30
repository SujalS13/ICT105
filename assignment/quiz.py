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

def ask_question(question_data):
    print(question_data['question'])
    for option in question_data['options']:
        print(option)
    user_answer = input("Your answer: ").strip().lower()
    correct_option = question_data['answer']
    correct_index = ['a', 'b', 'c', 'd'].index(correct_option)
    correct_text = question_data['options'][correct_index]
    return user_answer == correct_option, correct_text

def run_quiz(questions):
    score = 0
    i = 0
    for question_data in random.sample(questions, 10):
        i += 1
        print(f"\nQuestion {i}:")
        correct, correct_text = ask_question(question_data)
        if correct:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_text}")
        print(f"Your current score is {score}/{i}")
        user_input = input("Do you want to continue? (yes/no) or type 'quit' to exit: ").strip().lower()
        if user_input!= 'yes':
            if user_input == 'quit':
                print("You have quit the quiz.")
            break
    print(f"Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    file_path = 'quiz_question.txt'
    try:
        questions = read_questions_from_file(file_path)
        run_quiz(questions)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
