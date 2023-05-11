from .point import Point
import math


def find_lines(point, lines):
    """ Нахождение прямых в которых содержится данная точка """
    find_lines = list()
    for line in lines:
        if point in line:
            find_lines.append(line)
    return find_lines


def distance_point_to_line(point, line):
    """ Расстояние от точки до прямой """
    x0, y0 = point.getXY()
    x1, y1 = line.point1.getXY()
    x2, y2 = line.point2.getXY()

    numerator = (y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1
    denominator = math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

    return numerator / denominator
