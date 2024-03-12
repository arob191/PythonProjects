from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank =  []

for question in question_data:
    question = Question(question['text'], question['answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

more_questions = True

while more_questions:
    quiz.next_question()
    more_questions = quiz.still_has_questions()
