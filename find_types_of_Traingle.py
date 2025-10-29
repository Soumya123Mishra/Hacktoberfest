# Python program to classify a given triangle
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Utility method to return square of x
def square(x):
    return x * x

# Utility method to sort a, b, c; after this
# method a <= b <= c
def order(a, b, c):
    copy = [a, b, c]
    copy.sort()
    return copy[0], copy[1], copy[2]

# Utility method to return Square of distance
# between two points
def euclidDistSquare(p1, p2):
    return square(p1.x - p2.x) + square(p1.y - p2.y)

#  Method to classify side
def getSideClassification(a, b, c):
    # if all sides are equal
    if a == b and b == c:
        return "Equilateral"

    # if any two sides are equal
    elif a == b || b == c || a == c:
        return "Isosceles"
    else:
        return "Scalene"

#  Method to classify angle
def getAngleClassification(a, b, c):
  
    # If addition of sum of square of two side
    # is less, then acute
    if a + b > c:
        return "acute"

    # by pythagoras theorem
    elif a + b == c:
        return "right"
    else:
        return "obtuse"

# Method to classify the triangle by sides and angles
def classifyTriangle(p1, p2, p3):
  
    # Find squares of distances between points
    a = euclidDistSquare(p1, p2)
    b = euclidDistSquare(p1, p3)
    c = euclidDistSquare(p2, p3)

    # Sort all squares of distances in increasing order
    a, b, c = order(a, b, c)
    print("Triangle is ", getAngleClassification(a, b, c),
          " and ",  getSideClassification(a, b, c))

# Driver code
p1 = point(3, 0)
p2 = point(0, 4)
p3 = point(4, 7)
classifyTriangle(p1, p2, p3)

p1 = point(0, 0)
p2 = point(1, 1)
p3 = point(1, 2)
classifyTriangle(p1, p2, p3)

# The code is contributed by Gautam goel (gautamgoel962)
