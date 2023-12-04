from question_list import questions_and_answers
from question import Question
from QuestionMaster import QuestionMaster
question_bank = []

for qnD in questions_and_answers:
    q = qnD["question"]
    a = qnD["answer"]
    question_bank.append(Question(q, a))

question_master = QuestionMaster(q_list=question_bank)
question_master.start_quiz()