class QuizBrain:

    def __init__(self, q_list):
        self.qeustion_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.qeustion_number]
        self.qeustion_number += 1
        user_answer = input(f"Q.{self.qeustion_number}: {current_question.text} (True/False): ").lower()
        self.chech_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.qeustion_number < len(self.question_list)

    def chech_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")

        print(f"The correct answer was : {current_question}.")
        print(f"Your current score is: {self.score}/{self.qeustion_number}\n")