from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# Pause Challenge 2 Lesson 121: 4:30: Create a list of question objects from the data.

question_bank = []

for question in question_data:
    question_text = question["question"] # Changed from "text" to "question" for pause challenge 9
    question_answer = question["correct_answer"] # Changed from "answer" to "correct_answer" for pause challenge 9
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

# Pause challenge 8: Lesson 124: 7:02: Print the final score
print("You've completed the quiz!")
print(f"Final score: {quiz.score}/{quiz.question_number}")