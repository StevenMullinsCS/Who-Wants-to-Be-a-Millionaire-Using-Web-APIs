import requests
import json

points=0

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
    return points

def set_points(new_points):
    points = new_points

def set_difficulty():
    if get_points < 1000:
        difficulty = "EASY"
    # Placeholder
    elif str:
        return
def qna():
    # Print the question for the user

    #Placeholder
    return str