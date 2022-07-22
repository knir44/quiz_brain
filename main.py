from Question_moudle import Question
from model1 import question_data
from quiz_brain import QuizBrain

list1 = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    list1.append(Question(text, answer))

quiz = QuizBrain(list1)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.qeustion_number}")




