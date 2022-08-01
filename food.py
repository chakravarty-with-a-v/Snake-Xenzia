from turtle import Turtle
from random import randint
X = 230
Y = 230


class Food(Turtle):
    def __init__(self):
        super().__init__()  # Inheriting  Turtle class
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speed("fastest")
        x = randint(-X, X)  # RANDOM X AND Y CO-ORDINATES OF FOOD GENERATED
        y = randint(Y, Y)
        self.goto(x, y)

    def new_food(self):
        x = randint(-X, X)
        y = randint(-Y, Y)
        self.goto(x, y)
