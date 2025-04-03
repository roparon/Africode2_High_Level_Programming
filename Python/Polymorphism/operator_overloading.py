class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overloading the '*' operator
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # String representation for printing
    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Example usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Using the overloaded '+' operator
v3 = v1 + v2
print(v3)  # Output: Vector(6, 8)

# Using the overloaded '*' operator
v4 = v1 * 3
print(v4)  # Output: Vector(6, 9)