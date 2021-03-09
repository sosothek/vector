import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.norm = math.sqrt(x * x + y * y)
        self.arg = math.asin(y/self.norm)
        
    def scalar(self, v):
        return v.x * self.x + v.y * self.y




