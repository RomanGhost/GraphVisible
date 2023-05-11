import math


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def getXY(self, scale=1):
        return round(self.x * scale, 4), round(self.y * scale, 4)

    def copy(self):
        return Point(round(self.x, 4), round(self.y, 4))

    def getAngle(self, other):
        point1 = other - self
        # prinst(point1.getXY())
        try:
            res = round(math.acos(-point1.y / (math.sqrt(point1.x * point1.x + point1.y * point1.y))), 5)
        except ZeroDivisionError:
            res = 0

        if other.x > self.x:
            res = -res
        return res

    def __str__(self):
        return f"({float(round(self.x, 4))}, {float(round(self.y, 4))})"

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.getXY() == other.getXY()

    def __lt__(self, other):
        """ < """
        if self == other:
            return False
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x