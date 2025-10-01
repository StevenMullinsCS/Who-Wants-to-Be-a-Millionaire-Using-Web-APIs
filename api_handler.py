import requests
import json
import questions

# URLs for the different datasets used in the project based on difficulty
url_easy = "https://opentdb.com/api.php?amount=5&difficulty=easy&type=multiple"
url_medium = "https://opentdb.com/api.php?amount=5&difficulty=medium&type=multiple"
url_hard = "https://opentdb.com/api.php?amount=5&difficulty=hard&type=multiple"

def parse_question(difficulty):
    if difficulty == "EASY":
        qs = requests.get(url_easy)
        qs_json = qs.json()
        print(qs_json)
    elif difficulty == "MED":
        qs = requests.get(url_medium)

    else:
        requests.get(url_hard)




def build_question_set(set):
    questions = []
    for qs in set:
        questions.insert
