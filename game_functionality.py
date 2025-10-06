from re import match
from api_handler import parse_questions
import requests
import json

# Who Wants To Be A Millionaire uses a "Point Ladder" structure. The easiest way I figured out to do the points was to
# have a stack that pops the values as questions are answered correctly.
base_point_vals = [100, 200, 300, 500,                     # EASY
                   1000, 2000, 4000, 8000, 16000,          # MEDIUM
                   32000, 64000, 125000, 250000, 500000,   # HARD
                   1000000]                                # WIN CONDITION
user_points = 0
difficulty = "EASY"

questions_set = []

def restart():
    uinput = ""
    while(uinput != "Y" | uinput != "N"):
        uinput = input("Play Again? (Y/N): ")
        uinput = uinput.capitalize()
        if(uinput == "Y"):
            points=0
        elif(uinput == "N"):
            exit(0)
        else:
            uinput = input("Invalid input. Please try Enter Y or N.: ")


def get_points():
    return user_points

def set_points():
    i = 0
    #if difficulty == "ENDLESS":
      #  user_points = user_points + 100000
    #else:
    user_points = base_point_vals.pop()
    user_points += 1

def set_difficulty(points):
    if points == 1000:
        difficulty = "MEDIUM"
    elif points == 32000:
        difficulty = "HARD"
    else:
        return
    return difficulty

def check_answer(question, answer):
    if answer ==
def qna():
    if not questions_set:
        parse_questions(difficulty)
    else:
        q_index = 0
        print(questions_set[q_index])
        answer = input("Please select A, B, C, or D.")
        ans_as_int = answer.char - 64
        check_answer(questions_set[q_index], answer)
    #Placeholder
    return str




