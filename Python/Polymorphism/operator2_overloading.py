#Assignment
#Create a class that displays the ipmplementation of operator overloading in


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return "NotImplemented"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"


# Example usage
point1 = Point(3, 4)
point2 = Point(1, 2)

result = point1 + point2

print(result)  # Output: Point(x=4, y=6)
