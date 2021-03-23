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




