# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

'''
To take input: input("Message")

'''

# Ask the user on the size of the square

size = float(input("How big do you want the size of the triangle to be?"))

# Ask the user on the size of the pen

penSize = int(input("How big do you want the size of the painter to be?"))

painter.fillcolor("red")

painter.pensize(penSize)
painter.forward(size)
painter.left(120)
painter.forward(size)
painter.left(120)
painter.forward(size)

# create screen object and make it persist

wn = trtl.Screen()
wn.mainloop()