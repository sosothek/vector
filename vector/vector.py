import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.norm = math.sqrt(x*x + y*y)
        if x != 0 and y >= 0:
            self.arg = math.acos(x / self.norm)
        elif y != 0 and x > 0:
            self.arg = math.asin(y / self.norm)
        elif x < 0 and y < 0:
            self.arg = -math.acos(x / self.norm)
        else:
            self.arg = None

    def scalar(self, v):
        return self.x * v.x + self.y * v.y
