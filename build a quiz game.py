from quiz_model import Question
question_prompt = [
     "What a color of apple?\n(A) Red/Green \n(B) Pink \n(C) Blue\n",
     "What a color of banana?\n(A) Purple \n(B) Black \n(C) Yellow\n",
     "What a color of srawberry?\n(A) white\n(B) Red \n(C) orange\n",
]

questions = [
    Question(question_prompt[0], "A"),
    Question(question_prompt[1], "C"),
    Question(question_prompt[2], "B"),
]

def run_test(questions):
    score = 0
    for question in questions:
     answer = (input( question.prompt))
     if answer == question.answer:
         score += 1
    print(f"You got {score}/{len(questions)} correct")
run_test(questions)