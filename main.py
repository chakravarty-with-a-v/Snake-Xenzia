from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time
from score import Score
WALL_BOUNDARY = 260
# CREATING A BOUNDARY


def build_wall(x):
    wall = Turtle()
    wall.hideturtle()
    wall.penup()
    wall.pensize(2)
    wall.color("white")
    wall.goto(-x, x)
    wall.pendown()
    wall.goto(x, x)
    wall.goto(x, -x)
    wall.goto(-x, -x)
    wall.goto(-x, x)


# creating screen object
screen = Screen()
screen.tracer(0)  # to stop screen from showing animations
screen.setup(600, 600)  # screen size is set as 600*600
screen.bgcolor("black")  # screen background color is black
screen.title("THE GREEDY CORAL SNAKE")
snake = Snake()  # snake object created
food = Food()  # food object created
score = Score()
screen.update()  # to get initial positions of snake
build_wall(WALL_BOUNDARY)
screen.listen()  # to listen for keystrokes
screen.onkey(snake.right, "Right")  # move right on Right Arrow Key
screen.onkey(snake.left, "Left")  # move left on Left Arrow Key
screen.onkey(snake.up, "Up")  # move up on Up Arrow Key
screen.onkey(snake.down, "Down")  # move down on Down Arrow Key
while True:
    time.sleep(snake.speed)  # as snake eats fruit speed is updated by updating sleep time
    snake.unit_move()  # snake moves by 1 unit length
    screen.update()  # screen is updated to show change
    if snake.head.distance(food) < 15:  # default turtle size is 20 pixels so anything less than it = collision
        food.new_food()  # if snake eats fruit, new fruit is randomly generated
        score.increase_score()  # score is incremented by 1
        snake.increase()  # speed is increased
    if snake.wall_collision() or snake.snake_collision():  # if snake collides with wall or its own body
        screen.update()
        time.sleep(3)
        for segments in snake.snake_segments:
            segments.hideturtle()
        food.hideturtle()
        screen.update()
        # GAME OVER MESSAGE GENERATED
        game_over = Turtle()
        game_over.penup()
        game_over.hideturtle()
        game_over.color("white")
        game_over.write("GAME OVER !", align="center", font=("Arial", 30, "normal"))
        if snake.wall_collision():
            game_over.goto(0, -30)
            game_over.write("YOU HIT WALL BUILT WITH AMBUJA CEMENT !", align="center", font=("Arial", 14, "normal"))
        if snake.snake_collision():
            game_over.goto(0, -30)
            game_over.write("GREED MAKES US BLIND !", align="center", font=("Arial", 14, "normal"))
        if score.new_high_score():
            time.sleep(2)
            game_over.clear()
            score.update_high_score(game_over)
        break
screen.exitonclick()
