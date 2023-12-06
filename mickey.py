from turtle import *
# speed(0)
def mickey_emoji(): # function to draw a mickey mouse emoji 
    def draw(x,y,color,size): # draw mickey, passing (x,y) co-ordinates, with color and size
        penup()
        goto(x,y)
        pendown()
        begin_fill()
        fillcolor(color)
        circle(size)
        end_fill()

    draw(-500,-50,"#FFA07A",60) # draw the big circle (face of the mickey)
    draw(-435,40,"black",30) # draw the ears (left)
    draw(-565,40,"black",30) # draw the ears (right)
    draw(-530,20,"black",10) # draw the eye (left)
    draw(-470,20,"black",10) # draw the eye (right)

    # to draw the mouth (semi circle) 
    penup()
    goto(-533,-10)
    pendown()
    right(60)
    width(3) # defining the line thickness of the mouth
    circle(40,120)
    # hideturtle()
# penup()
# setposition(-200,0)
# pendown()

mickey_emoji()

done()