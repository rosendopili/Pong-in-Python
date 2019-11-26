import turtle
import os

win = turtle.Screen()
# sets variable name for the screen
win.title("Python Pong by Rosendo Pili")
# sets title screen
win.bgcolor("black")
# sets background color of window
win.setup(width=800, height=600)
# sets height and width of window
win.tracer(0)
# stops default window reset

# Score
score_a = 0
score_b = 0

# Paddle A
pad_a = turtle.Turtle()
# creating a variable name for Paddle A which is a turtle object.
pad_a.speed(0)
# sets speed of animation to max
pad_a.shape("square")
# sets paddle shape
pad_a.color("white")
# sets paddle color
pad_a.shapesize(stretch_wid=5, stretch_len=1)
# sets paddle dimensions
pad_a.penup()
# ensures that the turtle import does not draw a line when the paddle moves
pad_a.goto(-350, 0)
# sets a starting point for Paddle A (x coordinate, y coordinate)


# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2
# lines 47 & 48 setting delta values of and x & y coordinates of ball

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0      Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)
    # ycor turtle module functionality that returns the y coordinate of the object
    # sety sets the y coordinate to the new y location of the object

def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)

# Keyboard binding keys to movement functions
win.listen()
win.onkeypress(pad_a_up, "s")
win.onkeypress(pad_a_down, "z")
win.onkeypress(pad_b_up, "Up")
win.onkeypress(pad_b_down, "Down")

# Main Game Loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay pong.wav")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay pong.wav")
    # making the ball interact with the top and & bottom borders

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay pong.wav")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay pong.wav")





