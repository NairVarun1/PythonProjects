from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for i in range(len(question_data)):
    question = question_data[i]["text"]
    correct_answer = question_data[i]["answer"]
    new_question = Question(question, correct_answer)
    questionBank.append(new_question)

quiz = QuizBrain(questionBank)

while quiz.still_has_question():
    quiz.next_question()

if not quiz.still_has_question():
    print("You have completed the quiz !")
    print(f' Your final score is {quiz.score}/{len(questionBank)}')
