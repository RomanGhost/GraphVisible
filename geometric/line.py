from .point import Point


class Line:
    def __init__(self, p1: Point = None, p2: Point = None):
        self.point1 = p1
        self.point2 = p2

    def __eq__(self, other):
        return self.point1 == other.point1 and self.point2 == other.point2\
            or self.point1 == other.point2 and self.point2 == other.point1

    def lenght(self):
        x = self.point2.x - self.point1.x
        y = self.point2.y - self.point1.y

        return round((x * x + y * y) ** 0.5, 5)

    def __str__(self) -> str:
        return f"{self.point1} {self.point2}"

    def __contains__(self, point):
        return self.point1 == point or self.point2 == point

    def pointBelong(self, point: Point):
        max_x, min_x = self.point1.x, self.point2.x
        if min_x > max_x:
            max_x, min_x = min_x, max_x

        max_y, min_y = self.point1.y, self.point2.y
        if min_y > max_y:
            max_y, min_y = min_y, max_y

        return (point.x >= min_x <= max_x) and (min_y <= point.y <= max_y)

    def mid(self):
        return Point(self.point2.x - self.point1.x, self.point2.y - self.point1.y)

    # функция готова
    def collision(self, other):
        if self == other:
            return True
        def intersect(l1, l2):
            def ccw(a, b, c):
                return (c.y - a.y) * (b.x - a.x) >= (b.y - a.y) * (c.x - a.x)

            a, b, c, d = l1.point1, l1.point2, l2.point1, l2.point2
            return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)

        def segments_intersect(point1, point2, p3, p4):
            l1, l2 = Line(point1, point2), Line(p3, p4)
            if intersect(l1, l2):
                return True
            elif intersect(l2, l1):
                return True
            return False
        return intersect(self, other)

    def copy(self):
        return Line(self.point1.copy(), self.point2.copy())

    # создать перегрузку для сравненя двух прямых
