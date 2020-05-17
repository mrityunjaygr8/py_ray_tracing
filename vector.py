import math


class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __str__(self):
        return f"[{self.x}, {self.y}, {self.z}]"

    def __repr__(self):
        return self.__str__()

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        assert type(other) is float or type(other) is int
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        assert type(other) is float or type(other) is int
        return Vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        assert type(other) is float or type(other) is int
        return Vector(round(self.x / other, 3), round(self.y / other, 3), round(self.z / other, 3))

    def magnitude(self):
        return math.sqrt(self.dot(self))

    def normalized(self):
        magnitude = self.magnitude()
        return self / magnitude
