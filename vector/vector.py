import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.norm = math.sqrt(x * x + y * y)
        if self.y > 0:
            self.arg = math.acos(x/self.norm)
        else:
            self.arg = -math.acos(x/self.norm)

    def scalar(self, v):
        return v.x * self.x + v.y * self.y

    def __add__(self, v):
        x = v.x + self.x
        y = v.y + self.y
        return Vector(x, y)

    def __eq__(self, v):
        a = self.x == v.x
        i = self.y == v.y
        return a and i

    def __sub__(self, v):
        s = self.x - v.x
        j = self.y - v.y
        return Vector(s, j)

    def __mul__(self, a):
        h = a*self.x
        k = a*self.y
        return Vector(h, k)

    def __rmul__(self, a):
        return self*a

    def __rsub__(self, v):
        s = -self.x + v.x
        j = -self.y + v.y
        return Vector(s, j)

    def __truediv__(self, a):
        return self*(1/a)

    def exp(self):
        return Vector(1, 1)*math.cosh(self.norm) + (self/self.norm)*math.sinh(self.norm)


built_exp = math.exp


def newexp(x):
    if isinstance(x, Vector):
        return x.exp()
    else:
        return built_exp(x)


math.exp = newexp



