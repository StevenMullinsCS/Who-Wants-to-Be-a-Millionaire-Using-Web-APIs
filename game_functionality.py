"""
game_functionality.py contains the functions that allow the game to actually be playable.
"""

from re import match
from api_handler import parse_questions
from game_ui import win, lose
import requests
import json

# Who Wants To Be A Millionaire uses a "Point Ladder" structure. The easiest way I figured out to do the points was to
# have a stack that pops the values as questions are answered correctly.
base_point_vals = [0, 100, 200, 300, 500,                     # EASY
                   1000, 2000, 4000, 8000, 16000,          # MEDIUM
                   32000, 64000, 125000, 250000, 500000,   # HARD
                   1000000]                                # WIN CONDITION
difficulty = ""
questions_set = []
user_points = 0
lost = False
point_index = 0


'''
Resets the values of the program to allow the game to reset. If the game does not reset, the questions would be rehashed,
and the points would never be reset to 0, resulting in the difficulty never lowing to easy.'''
def restart():
    uinput = ""
    uinput = input("Play Again? (Y/N): ")
    uinput = uinput.capitalize()
    if uinput == "Y":
        global user_points
        global point_index
        global questions_set
        point_index = 0
        user_points = 0
        questions_set = []
    elif uinput == "N":
        exit(0)
    else:
        while uinput != "Y" and uinput != "N":
            print("Invalid input, please enter Y or N.")
            return restart()

'''
Checks the current difficulty of the game based on the number of points. Once the points crosses the thresholds listed,
the difficulty is changed to the corresponding value. This is used to determine the question set to be used as well as
display the win screen if the game is won.
'''
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

'''
Sets the points dependant on the amount of correctly answered questions, using the amount to call the array of possible
point values.
'''
def set_points():
    global user_points
    global point_index
    user_points = base_point_vals[point_index]
    point_index += 1

'''
Compares the inputted answer converted to an int to the correct answer to the question and returns a boolean value
'''
def check_answer(question, answer_int):
    if question.correct_ans == question.ans[answer_int]:
        return True
    else:
        return False

'''
Checks to see if the question set contains questions or not. If it does not, it calls a function to populate the question
set.
'''
def check_empty_set():
    if not questions_set:
        questions_set.extend(parse_questions(difficulty))
        return
    else:
        return

'''
Displays questions for the user to answer and accepts input for the answers to said questions.
Then calls a function to check the answer to ensure it is correct before displaying another question, or displaying a
win or loss screen
'''
def qna():
    check_difficulty()
    check_empty_set()
    lost = False
    while lost is False:
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
            lost = False
        else:
            lost = True
            return lose(user_points)







