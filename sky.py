import turtle
import random
t = turtle.Turtle()
w = turtle.Screen()
t.speed(0)
w.bgcolor("black")
t.color("white")
w.title("Starry Sky")
def stars():
    for i in range(8):
        t.fd(10)
        t.right(144)
for i in range(1000):
    x = random.randint(-1040, 1040)
    y = random.randint(-430, 430)
    stars()
    t.up()
    t.goto(x, y)
    t.down()
t.up()
t.goto(0, 170)
t.down()
t.color("white")
t.begin_fill()
t.circle(80)
t.end_fill()
t.hideturtle
w.exitonclick()
