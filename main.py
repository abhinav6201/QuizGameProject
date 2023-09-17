from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]['question'], question_data[i]['correct_answer']))

# print(question_bank[1].text)

QuizBrain_obj = QuizBrain(question_bank)

while QuizBrain_obj.still_has_questions():
    QuizBrain_obj.next_question()

print("Congratulations for completing the quiz")
print(f"Your final score is {QuizBrain_obj.score}/{QuizBrain_obj.question_number}")
