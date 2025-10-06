from inspect import stack

import requests
import json
from questions import Question
# URLs for the different datasets used in the project based on difficulty
url_easy = "https://opentdb.com/api.php?amount=5&difficulty=easy&type=multiple"
url_medium = "https://opentdb.com/api.php?amount=5&difficulty=medium&type=multiple"
url_hard = "https://opentdb.com/api.php?amount=5&difficulty=hard&type=multiple"

def check_response_code(response):
    if response.status_code == 200:
        return
    else:
        print(f"Error: Could not fetch questions set: Response Code {response.status_code}")
        exit(1)

# Calls the API depending on the current difficulty based on points. The data from the json will then be fed into the
# constructor for the question set. Using the API call necessary for the difficulty should help performance in theory,
# as there is not unnecessary data being stored when the questions are not needed yet.
def parse_questions(difficulty):
    if difficulty == "EASY":
        response = requests.get(url_easy)
        check_response_code(response)
        qs_json = response.json()
        return build_question_set(qs_json["results"])
    elif difficulty == "MED":
        qs = requests.get(url_medium)
    else:
        requests.get(url_hard)





def build_question_set(q_set):
    questions_set = []
    for qs in q_set:
        all_answers = qs["incorrect_answers"] + [qs["correct_answer"]]
        question = Question(
            q = qs["question"],
            diff = qs["difficulty"],
            ans = all_answers,
            correct = qs["correct_answer"]
        )
        questions_set.append(question)
    print(questions_set[0])
