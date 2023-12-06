from turtle import *
speed(0)
def draw_star(x, y):

    penup()
    setposition(x, y)
    pendown()

    begin_fill()
    fillcolor("#F6F1D5")
    for _ in range(5):
        forward(30)
        right(144)
    end_fill()

