import random

#questions and answers from the file imported
with open("quiz_question.txt", "r") as f:
    content = f.read()

questions = []
question = ""
answers = {}
for line in content.split("\n"):
    if line.startswith("Correct answer:"):
        answers[question] = line.split(": ")[-1]
    elif line.strip() and not line.startswith("Correct answer:"):
        if question:
            questions.append(question)
        question = line
questions.append(question)

# Select 10 random questions from set of 50 question
selected_questions = random.sample(questions, 10)

# Play the game
score = 0
for question in selected_questions:
    print(question)
    user_answer = input("Enter your answer (a/b/c/d): ").lower()
    correct_answer = answers[question][-1].lower()
    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")
    print()

# Display the final score
print(f"Your final score is {score} out of {len(selected_questions)}.")
    answer = input("Your answer (a/b/c/d): ").strip().lower()
    return answer == question['correct']

def run_quiz(quiz, num_questions=10):
    selected_questions = random.sample(quiz, num_questions)
    score = 0
    
    for i, question in enumerate(selected_questions, 1):
        print(f"\nQuestion {i}:")
        if ask_question(question):
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was {question['correct']}.")
        print(f"Your current score: {score}/{i}")
    
    print(f"\nFinal score: {score}/{num_questions}")

if __name__ == "__main__":
    quiz_filename = "quiz_questions.txt"
    quiz = load_quiz(quiz_filename)
    run_quiz(quiz)
