from turtle import *
import turtle as t

speed(0)

penup()
setposition(-450, 200)
write("Mickey Mouse thinking to eat icecream at night.",font=("Arial",30,))
pendown()

def cloud():
   

    t.Screen().bgcolor("#152074")
    speed(0)
    def filled_circle(radius, color):
        t.color(color,color)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

    radius = 30
    cloud_color="white"
    filled_circle(radius,cloud_color)
    t.forward(radius)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)
    filled_circle(radius,cloud_color)
    t.right(90)
    
    penup()
    setposition(-150,-80)
    pendown()
    filled_circle(10,cloud_color)
    penup()
    setposition(-180,-110)
    pendown()
    filled_circle(10,cloud_color)
    penup()
    setposition(-210,-150)
    pendown()
    filled_circle(10,cloud_color)

def ice_cream():
    #ice cream code
    #cone
    fillcolor('#6c3333')
    begin_fill()
    forward(100)
    right(120)
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

def Mickey():

    penup()
    setposition(-20, 120)
    pendown()

    def _draw(x,y,color,size):
        up()
        goto(x,y)
        down()
        begin_fill()
        fillcolor(color)
        circle(size)
        end_fill()

    _draw(-500,-50,"#FFA07A",60)
    _draw(-435,40,"black",30)
    _draw(-565,40,"black",30)
    _draw(-530,20,"black",10)
    _draw(-470,20,"black",10)


    up()
    penup()
    goto(-533,-10)
    pendown()
    right(60)
    # setheading(-60)
    width(3)
    down()
    circle(40,120)
    hideturtle()


def star():
    speed(0)
    def night():
        for _ in range(5):
            begin_fill()
            fillcolor("#F6F1D5")
            forward(30)
            right(144)
            forward(30)
            end_fill()

    penup()
    setposition(450, 10) #topleft
    pendown()
    night()

    penup()
    setposition(370, -50)#Bottomleft
    pendown()
    night()

    penup()
    setposition(580,10) #topright
    pendown()
    night()

    penup()
    setposition(510,-50) #Bottomright
    pendown()
    night()


penup()
setposition(-200,0)
pendown()

Mickey()
penup()
setposition(-100,0)
pendown()

cloud()

penup()
setposition(150,0)
right(60)
pendown()

ice_cream()
penup()
setposition(400,0)
pendown()
star()

done()