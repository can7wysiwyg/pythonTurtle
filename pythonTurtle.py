# pythonTurtle
""" Import the python Turtle library """
import turtle
""" create a polygon class """
class Polygon():
""" initialize the method """
  def __init__(self, name, sides):
     self.name = name
     self.sides = sides
""" Create a draw method to draw the polygon you'll instantiate"""
  def draw(self):
     for I in range(self.sides):
       turtle.forward(100)
       turtle.left(100)
     turtle.done()

""" Instantiate a polygon.. I'll use a square but you can use any you want!!!"""

Square = Polygon("Square", 4)

"""Call the draw method to see the Square drawn"""

Square.draw()
