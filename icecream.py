from turtle import *

def ice_cream():
    #ice cream code
    #cone
    fillcolor('#6c3333')
    begin_fill()
    for i in range(2): # Added a for loop to reduce repetitive lines of code
        forward(100)
        right(120)
    forward(100)
    right(25)
    end_fill()

    #icecream
    fillcolor('#ffc5d9')
    begin_fill()
    circle(-50,190)
    end_fill()

    #cherry
    penup()
    right(180)
    circle(50,95)
    pendown()
    fillcolor('red')
    begin_fill()
    circle(-5,360)
    end_fill()

ice_cream()