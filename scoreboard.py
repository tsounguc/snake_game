from turtle import Turtle
ALIGNMENT = "CENTER"
FONT = ("Courier", 24, "normal")
COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("data.txt") as file:
            content = file.read()
            self.high_score = int(content)

        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(0, 250)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color(COLOR)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
