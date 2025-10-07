from re import match
from api_handler import parse_questions
from game_ui import win, lose
import requests
import json

# Who Wants To Be A Millionaire uses a "Point Ladder" structure. The easiest way I figured out to do the points was to
# have a stack that pops the values as questions are answered correctly.
base_point_vals = [100, 200, 300, 500,                     # EASY
                   1000, 2000, 4000, 8000, 16000,          # MEDIUM
                   32000, 64000, 125000, 250000, 500000,   # HARD
                   1000000]                                # WIN CONDITION
difficulty = ""
questions_set = []
user_points = 0

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

def check_difficulty():
    global difficulty
    global user_points
    if user_points == 0:
        difficulty = "EASY"
    elif user_points == 1000:
        difficulty = "MEDIUM"
    elif user_points == 32000:
        difficulty = "HARD"
    elif user_points == 1000000:
        win()
    return difficulty

point_index = 0
def set_points():
    global user_points
    global point_index
    user_points = base_point_vals[point_index]
    point_index += 1

def check_answer(question, answer_int):
    if question.correct_ans == question.ans[answer_int]:
        return True
    else:
        return False

def qna():
    check_difficulty()
    if not questions_set:
        questions_set.extend(parse_questions(difficulty))
        return qna()
    else:
        lost = False
    while not lost:
        q_index = 0
        print(questions_set[q_index])
        valid_input = False
        while not valid_input:
            answer = input("Please select A, B, C, or D: ")
            answer = answer.upper()
            # Wanted to convert the letter inputted to the spot in the array, found how to do this through the stackoverflow link below:
            # https://stackoverflow.com/questions/20044730/convert-character-to-its-alphabet-integer-position
            if len(answer) != 1:
                answer = answer[0]
            ans_as_int = ord(answer) - 65
            if ans_as_int < 0 or ans_as_int > 3:
                print("Invalid input. Please try again.")
            else:
                valid_input = True
        correct = check_answer(questions_set[q_index], ans_as_int)
        if correct:
            set_points()
            questions_set.remove(questions_set[q_index])
            print(f"That was correct! Total Points: {user_points}\n"
                      f"Press enter to continue...")
            input()
            qna()
        else:
            lost = True
            return lose(user_points)







