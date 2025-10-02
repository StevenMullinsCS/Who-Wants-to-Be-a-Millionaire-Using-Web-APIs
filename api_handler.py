import requests
import json
from questions import Question
# URLs for the different datasets used in the project based on difficulty
url_easy = "https://opentdb.com/api.php?amount=5&difficulty=easy&type=multiple"
url_medium = "https://opentdb.com/api.php?amount=5&difficulty=medium&type=multiple"
url_hard = "https://opentdb.com/api.php?amount=5&difficulty=hard&type=multiple"

def parse_questions(difficulty):
    if difficulty == "EASY":
        qs = requests.get(url_easy)
        qs_json = qs.json()
        build_question_set(qs_json)
    elif difficulty == "MED":
        qs = requests.get(url_medium)

    else:
        requests.get(url_hard)




def build_question_set(set):
    questions_set = []
    for q in set:
        question = Question(
            qtext = q["question"],
            diff = q["diff"],
            ans = q["incorrect_answers"] + q["correct_answer"],
            correct = q["correct_answer"]
        )
        questions_set.insert(question)
    print(questions_set)
