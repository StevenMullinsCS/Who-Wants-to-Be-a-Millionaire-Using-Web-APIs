"""
questions.py contains the class that allows the questions from the API call to be used in the game. This seemed like
the best way to do it, as it allows us to call for certain parts easier and store the information easier.
"""
import random as rd
import html
# DEBUGGING: Display correct answer with question.
debug = True
class Question:
    qtext: str
    difficulty: str
    answers: list[str]
    correct_ans: str

    '''
    Initialize the Question object using the information from the JSON
    '''
    def __init__(self, q, diff, ans, correct):
        self.qtext = q
        self.diff = diff
        # Questions should not be in the same order as provided by the JSON. If they were, every question would be
        # correct if answered with A.
        self.ans = ans
        rd.shuffle(self.ans)
        self.correct_ans = correct

    '''
    Prints the question along with the answers from the list of possible answers. The user will input the corresponding
    letter associated with the answer given.
    '''
    def __repr__(self):
        if debug:
            return (f"{html.unescape(self.qtext)}\n"
                    f"\n"
                    f"A. {html.unescape(self.ans[0])}\n"
                    f"B. {html.unescape(self.ans[1])}\n"
                    f"C. {html.unescape(self.ans[2])}\n"
                    f"D. {html.unescape(self.ans[3])}\n"
                    f"CORRECT ANSWER: {self.correct_ans}\n")
        else:
            return (f"{html.unescape(self.qtext)}\n"
                f"\n"
                f"A. {self.ans[0]}\n"
                f"B. {self.ans[1]}\n"
                f"C. {self.ans[2]}\n"
                f"D. {self.ans[3]}\n")
