import math

class Shape:

    def __init__(self, color='yellow', filled = True):
        self.color = color
        self.filled = filled

    def getcolor(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def getfilled(self):
        return self.filled

    def setfilled(self, filled):
        self.filled = filled

    def tostring(self):
        if self.filled == True :
            return f"a shape with color of {self.color} and filled"
        else:
            return f"a shape with color {self.color} and not filled"

class circle(Shape):
    def __init__(self, color = "green", filled = True, radius = 1.0):
        super().__init__(color,filled)
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def tostring(self):
        return f"circle radius {self.radius}"

class rectangle(Shape):

    def __init__(self, color = "red",filled = True, width = 1.0, length = 2.0):
        super().__init__(color,filled)
        self.length = length
        self.width = width

    def getlength(self):
        return self.length

    def setlength(self, length):
        self.length = length

    def getwidth(self):
        return self.width

    def setwidth(self, width):
        self.width = width

    def getarea(self):
        return self.length * self.width

    def getperimeter(self):
        return 2 * (self.length + self.width)

    def tostring(self):
        return f"rectangle width = {self.width} and length = {self.length}"

def square (rectangle):

    def __init__(self,color = "blue", filled =True, width = 1.0, length = 1.0):
        super().__init__(color,filled,width,length)
        if self.length != self.width:
            self.length = self.width

    def getside(self):
        return self.width

    def setside(self,side):
        self.width = side
        self.length = side

    def setlength(self,side):
        self.length = side
        self.length = side

    def setwidth(self,side):
        self.width = side
        self.length = side

    def tostring(self):
        return f"square side = {self.length}"

def testCircle():
    print("this is a circle")
    Circle = circle()

def testRectangle():
    print("this is a rectangle")
    Rectangle = rectangle()
    print(rectangle.getcolor())
    print(rectangle.getarea())
    print(rectangle.getperimeter())

def testSquare():
    print("this is a square")
    Square = square()
    print(square.getside())
    square.setside(4.0)
    print(square.getside())
    print(square.getarea())
    print(square.getperimeter())

if __name__ == "__main__":
    testCircle()
    testRectangle()
    testSquare()

# what's wrong with this code :(
