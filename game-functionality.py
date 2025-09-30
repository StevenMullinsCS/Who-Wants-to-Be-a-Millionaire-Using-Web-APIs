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
