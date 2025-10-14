"""
main.py is where the game is ran from.
"""
from game_ui import welcome
import game_functionality as game

difficulty = "EASY"
game.set_points()
program_active = True
gameplay = True
'''
Loop to ensure that the program does not just stop after a question or two.
'''
while program_active:
    while gameplay:
        print("------------------------------------------")
        welcome()
        game.qna()
        game.restart()
        print("------------------------------------------")