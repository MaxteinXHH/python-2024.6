import turtle

def draw_heart():
    turtle.color("pink")
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.setheading(60)
    turtle.circle(-90, 200)
    turtle.forward(180)
    turtle.end_fill()
    turtle.done()

draw_heart()
