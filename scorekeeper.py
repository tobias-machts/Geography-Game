from turtle import Turtle
FONT = ('Arial', 24, 'bold')


class ScoreKeeper(Turtle):
    def __init__(self, position, max_score):
        super().__init__()
        self.score = 0
        self.max_score = max_score
        self.hideturtle()
        self.pu()
        self.goto(position)

    def add_score(self):
        """add 1 to the current score"""
        self.score += 1

    def write_score(self):
        """clears any pre-written text and writes the score at its current position"""
        self.clear()
        self.write(arg=f"Score: {self.score}", align="center", font=FONT)

    def get_score(self):
        """returns a string consisting of the current score a slash and the maximum score that can be reached"""
        return f"{self.score}/{self.max_score}"
