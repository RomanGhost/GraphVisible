from .point import Point
from .line import Line


class Figure:
    def __init__(self):
        self.points = list()
        # прямые для исключения
        self.exception = list()
        self.ribs = list()

    def appendPoint(self, point: Point):
        self.points.append(point)

        if len(self.points) <= 1:
            return
        if len(self.points) == 2:
            self.ribs.append(Line(*self.points))
            return
        if len(self.ribs) >= 3:
            self.ribs.pop()

        last_point = self.ribs[-1].point2
        first_point = self.ribs[0].point1
        self.ribs.append(Line(last_point, point))
        self.ribs.append(Line(point, first_point))

    def appendException(self, line: Line):
        self.exception.append(line)

    def createDiagonals(self):
        """ Создать диагонали которые не пересекают exception """
        diagonals = list()
        if len(self.points) <= 3:
            return diagonals

        for num1, p1 in enumerate(self.points):
            for num2, p2 in enumerate(self.points):
                if num1 < num2:
                    break
                if p1 is p2:
                    continue

                if self.isRib(p1, p2):
                    continue

                collis = False
                res_line = Line(p1, p2)
                for l in self.exception:
                    if res_line.collision(l):
                        collis = True
                        break

                if not collis:
                    diagonals.append(res_line)

        return diagonals

    def existPoint(self, point):
        for p in self.points:
            if p.getXY() == point.getXY():
                return True
        return False

    def isRib(self, point1, point2):
        for rib in self.ribs:
            if ((rib.point1.getXY() == point1.getXY() and rib.point2.getXY() == point2.getXY())
                    or (rib.point1.getXY() == point2.getXY() and rib.point2.getXY() == point1.getXY())):
                return True
        return False
