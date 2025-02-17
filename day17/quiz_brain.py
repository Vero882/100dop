#

# Pause challenge 4: Lesson 122: 2:15: Create a quiz brain class
# Pause challenge 5: Lesson 122: 4:00: Create a method called next_question
# Pause challenge 6: Lesson 123: 1:50: Create a method called still_has_questions
# Pause challenge 7: Lesson 124: 3:57: Implement scoring

class QuizBrain:
    def __init__ (self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ").lower()
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
