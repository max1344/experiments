
from student import Question


question_prompts = [
    "What color are apples?\n (a) green \n (b) Purple \n (c) Magenda \n\n",
    "What color are bananas?\n (a) red \n (b) yellow \n (c) orange \n\n",
    "What color are your feet?\n (a) white \n (b) black \n (c) brown \n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]



def run_test(questions):
    score = 0
    for question in questions:
        answer = (input(question.prompt))
        if answer == question.answer:
            score += 1


    print("You got " + str(score) + "/" + str(len(questions)))

run_test(questions)