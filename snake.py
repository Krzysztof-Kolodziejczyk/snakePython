import turtle
from settings import *
from random import randint
import time

wn = turtle.Screen()
wn.title("snake")
wn.bgcolor("yellow")
wn.setup(WIDTH, HEIGTH)
wn.tracer(0, 10)


gameOver = turtle.Turtle()
gameOver.hideturtle()
# sanke head

head = turtle.Turtle()
head.shape("circle")
head.color("blue")
head.penup()
head.goto(0, 0)
head.speed(0)
head.direction = "stop"

# food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(randint(-250, 250), randint(-250, 250))

# semgents
segments = []

# pen

pen = turtle.Turtle()
pen.color("black")
pen.speed(0)
pen.shape("circle")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("score 0  High Score 0", align="center", font=("Courier", 30, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


# move
def move(s):
    if head.direction != "stop":
        gameOver.clear()
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + s)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - s)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - s)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + s)


# keyboard

wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

speed = 20
score = 0
highscore = 0
while True:
    wn.update()
    move(speed)
    if head.distance(food) < 20:
        food.goto(randint(-250, 250), randint(-250, 250))
        speed += 0.2
        score += 1
        pen.clear()
        pen.write("score {}  High Score {}".format(score, highscore), align="center", font=("Courier", 30, "normal"))
        new_segment = turtle.Turtle()
        new_segment.shape("circle")
        new_segment.color("blue")
        new_segment.penup()

        new_segment.speed(0)
        segments.append(new_segment)

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    time.sleep(0.1)


    if head.xcor() > 290 or head.xcor() < (-290) or head.ycor() > 290 or head.ycor() < (-290):
        head.goto(0, 0)
        for x in segments:
            x.goto(4000, 4000)
        segments.clear()
        if score > highscore:
            highscore = score
            pen.clear()
            pen.write("score {}  High Score {}".format(0, highscore), align="center", font=("Courier", 30, "normal"))
        score = 0
        head.direction = "stop"
        speed = 3

        gameOver = turtle.Turtle()
        gameOver.clear()
        gameOver.color("pink")
        gameOver.speed(0)
        gameOver.shape("circle")
        gameOver.penup()
        gameOver.hideturtle()
        gameOver.goto(0, 0)
        gameOver.write("game over", align="center", font=("Courier", 70, "normal"))


wn.mainloop()
