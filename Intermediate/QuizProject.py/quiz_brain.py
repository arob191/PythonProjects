class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        user_answer = input((f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False):" ))
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1
    
    def still_has_questions(self):
        # This will either be returned as True or False:
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_answer, current_answer):
        # This will either be returned as True of False:
        if user_answer.lower() == current_answer.lower():
            self.score +=1
            print("You are correct!")
        else:
            print("You are wrong!")
        print(f"The correct answer is {current_answer}.")
        print(f"Your current score is: {self.score} / {self.question_number + 1}")
        print("")