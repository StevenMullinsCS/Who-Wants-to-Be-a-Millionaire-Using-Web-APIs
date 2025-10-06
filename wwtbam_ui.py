def welcome():
    print("------------------------------------------------------\n"
      "|     Welcome to Who Wants to Be a Millionaire!      |\n"
      "|                                                    |\n"   
      "|      You will be asked multiple choice questions   |\n"
      "|     across a variety of subjects. For each correct |\n"
      "|     answer, you will be awarded a number of points.|\n"
      "|     As the game continues, the questions will get  |\n"
      "|     get harder, so be prepared! Can you answer the |\n"
      "|     Million Dollar Question? Good Luck!            |\n"
      "|                                                    |\n"
      "|     1. Play                                        |\n"
      "|     2. Credits                                     |\n"
      "|     3. Exit                                        |\n"
      "------------------------------------------------------\n")
    user_inp = input("Please select 1,2, or 3: ")
    if user_inp == 2:
        game_credits()
    elif user_inp == 3:
        exit(0)

def game_credits():
    print("------------------------------------------------------\n"
          "|                                                    |\n"
          "|         Who Wants To Be a Millionaire?             |\n"
          "|        Program created by Steven Mullins           |\n"
          "|                                                    |\n"
          "|    This application is a personal project          |\n"
          "|    inspired by the television game show \"Who       |\n"
          "|    Wants to Be a Millionaire?\". It is not          |\n"
          "|    affiliated with, endorsed by, or connected      |\n"
          "|    to Sony Pictures Television or any of its       |\n"
          "|    affiliated companies. For personal and          |\n"
          "|    non-commercial use only.                        |\n"
          "|                                                    |\n"
          "|    API provided by the fine folks at PixelTail     |\n"
          "|    Games under the Creative Commons License:       |\n"
          "|    https://creativecommons.org/licenses/by-sa/4.0/ |\n"
          "|    https://opentdb.com/                            |\n"
          "|    https://www.pixeltailgames.com/                 |\n"
          "|                                                    |\n"
          "|    Press Enter to return to game menu.             |\n"
          "|                                                    |\n"
          "------------------------------------------------------\n")
    input()
    return

def win():
    print("------------------------------------------------------\n"
          "|                                                    |\n"
          "|             Congratulations! You win!              |\n"
          "|            Would you like to play again?           |\n"
          "|                                                    |\n"
          "------------------------------------------------------\n")

def lose():
    print("------------------------------------------------------\n"
          "|                                                    |\n"
          "|       Unfortunately, That was incorrect.           |\n"
          "|        You walk away with winnings of:             |\n"
          "|                 $POINT PLACEHOLDER                 |\n"
          "|            Would you like to play again?           |\n"
          "|                                                    |\n"
          "------------------------------------------------------\n")