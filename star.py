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

positions = [(450, 10), (370, -50), (580, 10), (510, -50)]
for position in positions:
    draw_star(*position)

done()
# def main():
#     """
#     Main function to draw stars at specified positions.
#     """
#     turtle.speed(0)

#     # Coordinates for stars
#     positions = [(450, 10), (370, -50), (580, 10), (510, -50)]

#     # Draw stars at each position
#     for position in positions:
#         draw_star(*position)

#     turtle.done()

# if __name__ == "__main__":
#     main()