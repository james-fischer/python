class Point(object):
    """Represents a point in 2-D Cartesian space.
    """


    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = x


    def __str__(self):
        return("(%g , %g)" % (self.x, self.y))


    def __add__(self, other):
        temp = Point()
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        return temp

p = Point()
p.x = 3
p.y= 10


print(p)

p1 = Point()
p1.x = 5
p1.y = 6




print(p+p1)
