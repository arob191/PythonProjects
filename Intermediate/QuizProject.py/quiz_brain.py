class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
    
    def next_question(self):
        input((f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False):" )).lower()
        self.question_number += 1
    
    def still_has_questions(self):
        if self.question_number <= len(self.question_list):
            return True
        else:
            return False