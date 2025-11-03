import turtle

# 创建一个新的turtle对象
t = turtle.Turtle()

# 设置速度
t.speed(1)

# 设置颜色
t.color("red", "pink")

# 设置画笔粗细
t.pensize(2)

# 开始绘制爱心
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-100, 200)
t.left(120)
t.circle(-100, 200)

t.goto(0,0)
t.end_fill()

# 隐藏画笔
t.hideturtle()

# 保持窗口打开
turtle.done()










