import turtle
import random

def drawSquare(x, y, length, color):
    '''Draws a square with the desired color.'''
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(x, y)
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(x+length, y)
    myTurtle.goto(x+length, y+length)
    myTurtle.goto(x, y+length)
    myTurtle.goto(x, y)
    myTurtle.end_fill()

def sierpinski(x, y, side, degree):
    '''Draws Squares to make a sierpinski square.'''
    drawSquare(x, y, side, palette[degree])
    if degree > 0:
        sierpinski(x, y+side/2, side/2, degree-1)
        sierpinski(x+side/2, y+side/2, side/2, degree-1)
        sierpinski(x+side/2, y, side/2, degree-1)
    
if __name__ == '__main__':
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    palette = ['white', 'purple', 'blue', 'green', 'yellow', 'orange','red']
    sierpinski(-150, -150, 400, 6)
    myWin.exitonclick()
    
