import turtle
t = turtle.Turtle()
t.shape("turtle")


shape = input('도형을 입력하시오: ')
if shape == '사각형':
    width = int(input('가로: '))
    height = int(input('세로: '))
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)

elif shape == '삼각형':
    length = int(input('한 변의 길이: '))
    t.forward(length)
    t.left(120)
    t.forward(length)
    t.left(120)
    t.forward(length)

elif shape == '원':
    radius = int(input('반지름의 길이: '))
    t.circle(radius)

turtle.mainloop()
turtle.bye()
