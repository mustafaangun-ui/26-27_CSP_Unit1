#   Add your code here and add comments to your code
#   to describe what each section of code is doing

# import the turtle module
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

circlesize = float(input("what size should the base be? "))
pensize = float(input("what should the size of the pen be? "))
pencolor = str(input("what color should the pen be? "))

painter.pensize(pensize)
painter.color(pencolor)
painter.circle(circlesize)
painter.left(46)
painter.forward(147)
painter.left(92)
painter.forward(147)
painter.left(92)
painter.forward(147)
painter.left(92)
painter.forward(147)
painter.left(135)
painter.forward(205)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()