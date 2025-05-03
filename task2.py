import turtle


def draw_pifagor_tree(t, length, angle, level):
    """
    Recursively draws a Pifagor tree
    """
    if level == 0:
        return

    t.forward(length)

    pos = t.position()
    heading = t.heading()

    t.right(angle)
    draw_pifagor_tree(t, length * 0.8, angle, level - 1)

    t.penup()
    t.setposition(pos)
    t.setheading(heading)
    t.pendown()
    t.right(-angle)
    draw_pifagor_tree(t, length * 0.8, angle, level - 1)


def main():
    try:
        recursion_level = int(input("Enter the recursion level (recommended 5-8): "))
        if recursion_level < 1:
            recursion_level = 5
            print("The recursion level must be positive. Default value set to 5")
    except ValueError:
        recursion_level = 5
        print("Incorrect value entered. Default value set to 5")

    window = turtle.Screen()
    window.title("Pifagor tree")
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.color("green")

    t.penup()
    t.goto(0, -200)
    t.left(90)
    t.pendown()

    draw_pifagor_tree(t, 90, 45, recursion_level)

    t.hideturtle()

    window.mainloop()


if __name__ == "__main__":
    main()
