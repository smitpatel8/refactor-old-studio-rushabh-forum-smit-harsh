from turtle import *
import turtle as t

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
    for i in range (4): #Implemented for loop for reducing the repeated code for creating a cloud
        filled_circle(radius,cloud_color)
        t.right(90)
    def position(): #Created a function to move the cursor to make circle and color it for making small part of cloud to reduce the redundancy.
        pendown()
        filled_circle(10,cloud_color)
        penup() 
    penup()
    setposition(-150,-80)
    position()
    setposition(-180,-110)
    position()
    setposition(-210,-140)
    position()

