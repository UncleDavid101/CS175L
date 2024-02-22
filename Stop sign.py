import math
import turtle

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10

s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)

BORDER_WIDTH = (diameter - LENGTH) / 2

t = turtle.Turtle()



t.penup()
t.goto(-48 - BORDER_WIDTH, 117 - BORDER_WIDTH)
t.pendown()

t.color("red", "white")
t.begin_fill()
for _ in range(NUM_SIDES):
    t.forward(diameter - 1.8 * BORDER_WIDTH)
    t.right(ANGLE)
t.end_fill()

t.penup()
t.goto(-40 - BORDER_WIDTH, 100 - BORDER_WIDTH)
t.pendown()

t.color("red")
t.begin_fill()
for _ in range(NUM_SIDES):
    t.forward(diameter - 2 * BORDER_WIDTH)
    t.right(ANGLE)
t.end_fill()

t.penup()
t.goto(-60, -100)
t.color("white")
t.write("STOP", align="center", font=("Arial", 24, "bold"))

turtle.done()
