import turtle as trtl

color1 = "green"
color2 = "purple"

wn = trtl.Screen()
width = 1000
height = 1000

painter = trtl.Turtle()
painter.speed(0)
painter.color(color1)

answer = "y"
# loop until the user is bored
while (answer == "y"):
    # erase what is on the current window
    wn.clearscreen()
    # start in the middle
    painter.goto(0, 0)
    # Set up the space counter
    space = 1

    # get angle from the user
    angle = int(input("angle:"))
    seg = int(360 / angle)

    while painter.ycor() < height:
       if space % 100 == 0:
        painter.fillcolor(color2)
        painter.color(color2)


       if space % 200 == 0:
        painter.fillcolor(color1)
        painter.color(color1)

       painter.right(angle)
       painter.forward(2 * space + 10)  # experiment
       painter.begin_fill()
       painter.circle(3)
       painter.end_fill()
       space = space + 1

    answer = input("again?")

wn.bye()