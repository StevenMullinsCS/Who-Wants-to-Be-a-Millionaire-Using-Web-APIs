from game_ui import welcome, game_credits
import game_functionality as game
from api_handler import parse_questions, build_question_set
difficulty = "EASY"
game.set_points()
program_active = True
gameplay = True

while(program_active):
    welcome()
    while(gameplay):
        print("------------------------------------------")
        game.qna()
        print("------------------------------------------")