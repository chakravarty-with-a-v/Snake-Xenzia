from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("HighScore.txt", mode="r") as hs:
            high_score = int(hs.read())
        self.highScore = high_score
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"SCORE={self.score} | HIGH SCORE = {self.highScore} ", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def new_high_score(self):
        return self.score > self.highScore

    def update_high_score(self, game_over_turtle):
        if self.new_high_score():
            self.highScore = self.score
            with open("HighScore.txt", mode="w") as hs:
                hs.write(f"{self.highScore}")
            game_over_turtle.write(f" CONGRATULATIONS YOU SET A NEW HIGH SCORE={self.highScore} ", align="center",
                                   font=("Arial", 14, "normal"))
            self.clear()
            self.update_score()
