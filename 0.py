

import turtle

# Tạo đối tượng Turtle
t = turtle.Turtle()

# Đặt màu nền
turtle.bgcolor("black")

# Đặt màu vẽ và độ dày đường
t.color("red")
t.pensize(3)

# Di chuyển về vị trí ban đầu
t.penup()
t.goto(0, -200)
t.pendown()

# Vẽ trái tim
t.begin_fill()
t.fillcolor("blue")
t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.forward(224)
t.end_fill()

# Ẩn turtle
t.hideturtle()

# Hiển thị cửa sổ đồ họa
turtle.done()
