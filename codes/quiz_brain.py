class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        game_on = True
        while game_on and self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True or False)?: ")
            self.check_answer(answer, current_question.answer)
            self.question_number += 1
            if self.question_number == len(self.question_list):
                print("\n")
                print(f"You've completed the quiz! Your final score was: {self.score}/{self.question_number}.")
                game_on = False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("\n")
            print(f"You were right! Your current score is: {self.score}/{self.question_number + 1}.")
        else:
            print("\n")
            print(f"You were wrong. Your current score is: {self.score}/{self.question_number + 1}.")




#TODO: checking if the answer was correct
#TODO: checking if we are at the end of the quiz
