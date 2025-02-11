from turtle import *
from random import random, randint

screen = Screen()
width, height = 800, 600
screen.setup(width, height)
screen.title("两情若是久长时，又岂在朝朝暮暮")
screen.bgcolor("black")
screen.mode("logo")
screen.delay(0)  # 这里要设为0，否则很卡

t = Turtle(visible=False, shape='circle')
t.pencolor("blue")
t.fillcolor("white")
t.penup()
t.setheading(-90)
t.goto(width / 2, randint(-height / 2, height / 2))

stars = []
for i in range(200):
    star = t.clone()
    s = random() / 3
    star.shapesize(s, s)
    star.speed(int(s * 10))
    star.setx(width / 2 + randint(1, width))
    star.sety(randint(-height / 2, height / 2))
    star.showturtle()
    stars.append(star)

while True:
    for star in stars:
        star.setx(star.xcor() - 3 * star.speed())
        if star.xcor() < -width / 2:
            star.hideturtle()
            star.setx(width / 2 + randint(1, width))
            star.sety(randint(-height / 2, height / 2))
            star.showturtle()

1