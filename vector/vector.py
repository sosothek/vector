import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.norm = math.sqrt(x*x + y*y)
        if x == 0 and y == 0:
            self.arg = None
        elif x > 0 and y == 0:
            self.arg = 0
        elif x == 0 and y > 0:
            self.arg = math.pi / 2.
        elif x < 0 and y == 0:
            self.arg = math.pi
        elif x == 0 and y < 0:
            self.arg = -math.pi / 2.
        elif y > 0:
            self.arg = math.acos(x / self.norm)
        else:
            self.arg = -math.acos(x / self.norm)

    def scalar(self, v):
        return self.x * v.x + self.y * v.y
