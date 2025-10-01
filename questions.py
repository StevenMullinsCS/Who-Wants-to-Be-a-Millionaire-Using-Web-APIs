import random
class question():
    question: str
    difficulty: str
    answers: list[str]
    correct_ans: str


    def __init__(self, q, diff, ans, correct):
        self.question = q
        self.diff = diff
        self.ans = random.shuffle(ans)
        self.correct_ans = correct

    def __repr__(self):
        return (f"{question}\n"
                f"\n"
                f"A. {self.ans[0]}\n"
                f"B. {self.ans[1]}\n"
                f"C. {self.ans[2]}\n"
                f"D. {self.ans[3]}\n")
