from turtle import *
import turtle as t
from cloud import *
from icecream import *
from mickey import *
from star import *

speed(0)
penup()
setposition(-450, 200)
write("Mickey Mouse thinking to eat icecream at night.",font=("Arial",30,))
pendown()

penup()
setposition(-200,0)
pendown()

mickey_emoji()
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

positions = [(450, 10), (370, -50), (580, 10), (510, -50)]
for position in positions:
    draw_star(*position)

hideturtle()
done()