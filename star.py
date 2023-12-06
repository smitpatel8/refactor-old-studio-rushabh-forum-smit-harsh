import turtle
def draw_star(x, y):
    """
    Draws the star at the specified (x, y) position.
    """
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()

    turtle.begin_fill()
    turtle.fillcolor("#F6F1D5")
    for _ in range(5):
        turtle.forward(30)
        turtle.right(144)
    turtle.end_fill()

def main():
    """
    Main function to draw stars at specified positions.
    """
    turtle.speed(0)

    # Coordinates for stars
    positions = [(450, 10), (370, -50), (580, 10), (510, -50)]

    # Draw stars at each position
    for position in positions:
        draw_star(*position)

    turtle.done()

if __name__ == "__main__":
    main()