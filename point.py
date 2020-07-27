import math

class Point:
# Represents a point in a two-dimensional geometric coordinates


  def __init__(self,x=0, y=0):
    """Initialize the position of a new point. The x and y
    coordinates can be specified. If they are not, the point defaults to the origin."""
    self.move(x,y)

  def move(self,x,y):
    "Move the point to a new location in 2D space"
    self.x= x
    self.y= y

  def reset(self):
    "Reset the point back to the geometric origin: 0, 0"
    self.move(0,0)

  def calculate_distance(self, other_point):
     """ Uses the Pythagorean Theroem to calculate the distance between
     the two points. """
     return math.sqrt(
         (self.x - other_point.x) ** 2
        + (self.y -other_point.y) ** 2
         )  

# constructing a point
point= Point(3,5)
print(point.x, point.y)

point2=Point(4,5)
print(point2.x,point2.y)

print(point2.calculate_distance(point))


