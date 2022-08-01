from turtle import Turtle
INITIAL_POINTS = ((0, 0), (-20, 0), (-40, 0))
MOVE = 20


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create()
        self.head = self.snake_segments[0]
        self.snake_segments[1].color("magenta")
        self.speed = 0.1
        self.head.color("magenta")  # HEAD AND NEXT SEGMENT OF THIS SNAKE IS MAGENTA

    def create(self):
        for each_x in INITIAL_POINTS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(each_x)
            self.snake_segments.append(segment)

    def unit_move(self):
        for index in range(len(self.snake_segments)-1, 0, -1):
            # GETTING X AND Y CO-ORDINATES OF LAST BODY SEGMENT
            prev_x = self.snake_segments[index-1].xcor()
            prev_y = self.snake_segments[index - 1].ycor()
            self.snake_segments[index].goto(prev_x, prev_y)
        self.head.forward(MOVE)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def increase(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        last_x = self.snake_segments[len(self.snake_segments)-1].xcor()
        last_y = self.snake_segments[len(self.snake_segments) - 1].ycor()
        new_segment.goto(last_x, last_y)
        self.snake_segments.append(new_segment)
        self.speed *= 0.9
        self.unit_move()

    # CREATING A NEW BODY PART AT THE END
    def snake_collision(self):
        for index in range(1, len(self.snake_segments)):
            if self.head.distance(self.snake_segments[index]) < 15:
                self.snake_segments[index].color("red")
                return True

    def wall_collision(self):
        if self.head.xcor() > 240 or self.head.xcor() < -240 or self.head.ycor() > 240 or self.head.ycor() < -240:
            self.head.color("red")
            return True
