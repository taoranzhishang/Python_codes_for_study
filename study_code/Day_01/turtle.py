#import turtle
#turtle.write()只能打印字符串
#turtle.showturtle()
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.penup()
# turtle.goto(100,100)
# turtle.pendown()
# turtle.color("red")
# turtle.goto(100,-100)
# turtle.color("green")
# turtle.goto(-100,-100)
# turtle.color("yellow")
# turtle.goto(-100,100)
# turtle.color("pink")
# turtle.goto(100,100)

# turtle.penup()
# turtle.goto(0,-200)
# turtle.pendown()
# turtle.circle(200)

# 奥运五环
# turtle.penup()
# turtle.goto(-90, 0)
# turtle.pendown()
# turtle.color("blue")
# turtle.circle(50)
#
# turtle.penup()
# turtle.goto(0, 0)
# turtle.pendown()
# turtle.color("black")
# turtle.circle(50)
#
# turtle.penup()
# turtle.goto(90, 0)
# turtle.pendown()
# turtle.color("red")
# turtle.circle(50)
#
# turtle.exitonclick()

import turtle as t
t.pensize(4)
t.hideturtle()
t.colormode(255)
t.color((0,0,0), "black")
t.setup(600, 600)
t.speed(3)
t.setx(-130)
t.goto(-110,110)
t.goto(-90,110)
t.goto(-100,30)
t.goto(-90,125)
t.goto(-70,125)
t.goto(-70,43)
t.goto(-70,200)
t.goto(-50,200)
t.goto(-50,43)
t.goto(-50,125)
t.goto(-30,125)
t.goto(-10,30)
t.goto(-30,110)
t.goto(10,110)
t.goto(30,0)
t.goto(120,-180)
t.goto(90,-180)
t.goto(-50,0)
t.end_fill()
t.exitonclick()
