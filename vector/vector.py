import math
from typing import Union


class Vector:

    PRECISION = 6

    # noinspection PyTypeChecker
    def __init__(self, x: Union[int, float, "Vector"], y: Union[int, float] = None):
        if y is None and not isinstance(x, Vector):
            raise ValueError("Please specify y or give a Vector as first argument")
        if y is None:
            self.x = x.x
            self.y = x.y
            self.r = x.norm
            self.arg = x.arg
            return
        self.x = x
        self.y = y
        self.norm = math.sqrt(x * x + y * y)
        if x == 0 and y == 0:
            self.arg = None
        elif x > 0 and y == 0:
            self.arg = 0
        elif x == 0 and y > 0:
            self.arg = math.pi / 2.0
        elif x < 0 and y == 0:
            self.arg = math.pi
        elif x == 0 and y < 0:
            self.arg = -math.pi / 2.0
        elif y > 0:
            self.arg = math.acos(x / self.norm)
        else:
            self.arg = -math.acos(x / self.norm)

    def scalar(self, v):
        return self.x * v.x + self.y * v.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        return self - other

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __pos__(self):
        return Vector(self.x, self.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("Can only multiply a vector by an number")

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self * (1 / other)

    def __idiv__(self, other):
        return self * (1 / other)

    def __eq__(self, other):
        # noinspection PyTypeChecker
        return round(self.x, Vector.PRECISION) == round(other.x, Vector.PRECISION) and round(
            self.y, Vector.PRECISION
        ) == round(other.y, Vector.PRECISION)

    def __neq__(self, other):
        return not self == other

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def rotate(self, theta):
        # noinspection PyTypeChecker
        return Vector(
            self.x * math.cos(theta) - self.y * math.sin(theta), self.y * math.cos(theta) + self.x * math.sin(theta)
        )

    def exp(self):
        return Vector(1, 1) * math.cosh(self.norm) + (self / self.norm) * math.sinh(self.norm)


builtin_exp = math.exp


def newexp(x):
    if isinstance(x, Vector):
        return x.exp()
    else:
        return builtin_exp(x)


math.exp = newexp
