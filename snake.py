from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for index in range(3):
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.goto(x=index * -20, y=0)
            self.snake_segments.append(square)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)