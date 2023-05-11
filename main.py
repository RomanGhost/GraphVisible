import re
import pygame

import config
from data import Graph
from geometric import Point, Line

# чтение фигур и точек из файла
diagonals = list()
lines = list()

graph = Graph()
with open(config.cache_line, 'r') as file:
    x_s, y_s, x_e, y_e = map(float, re.findall(r"\d+.\d+", file.readline()))
    point_start = Point(x_s, y_s)
    point_end = Point(x_e, y_e)

    graph.addTop(point_start)
    graph.addTop(point_end)
    new_line = file.readline()
    for point_str in new_line.split(";"):
        x, y = map(float, re.findall(r"\d+.\d+", point_str))
        point = Point(x, y)
        graph.addTop(point)

    new_line = file.readline()
    for line_str in new_line.split(";"):
        x1, y1, x2, y2 = map(float, re.findall(r"\d+.\d+", line_str))
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)

        line = Line(p1, p2)

        lines.append(line)

    new_line = file.readline()
    for diagonal_str in new_line.split(";"):
        x1, y1, x2, y2 = map(float, re.findall(r"\d+.\d+", diagonal_str))
        diagonals.append(Line(Point(x1, y1), Point(x2, y2)))
        continue

# полное построение графа
with open(config.cache_graph, 'r') as file:
    n = int(file.readline())

    for i in range(n):
        arcs = file.readline()
        for arc in arcs.split(";"):
            num1, num2 = arc.split(",")
            num1 = int(num1)
            num2 = float(num2)

            graph.connect(i, num1, num2)

# считывание пути
with open(config.cache_way, 'r') as file:
    weight = file.readline()

    new_line = file.readline()
    way = list(map(int, new_line.split(',')))

pygame.init()
display = pygame.display.set_mode((1080, 600))
pygame.display.update()

scale = config.scale

game_run = True
while game_run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

    for d in diagonals:
        pygame.draw.line(display, (125, 125, 125), d.point1.getXY(scale), d.point2.getXY(scale), 6)

    for l in lines:
        pygame.draw.line(display, (125, 125, 125), l.point1.getXY(scale), l.point2.getXY(scale), 5)

    for p in graph.tops:
        pygame.draw.circle(display, (255, 255, 0), p.getXY(scale), 3)

    for num, indexes in enumerate(graph.connections):
        for index in indexes:
            pygame.draw.line(display, (0, 255, 0), graph.tops[num].getXY(scale), graph.tops[index.key].getXY(scale), 2)

    num = 1
    while num < len(way):
        pygame.draw.line(display, (255, 0, 0), graph.tops[way[num - 1]].getXY(scale),
                         graph.tops[way[num]].getXY(scale), 6)
        num += 1

    pygame.draw.circle(display, (0, 0, 255), point_start.getXY(scale), 5)
    pygame.draw.circle(display, (255, 255, 255), point_end.getXY(scale), 5)

    pygame.time.wait(1)
    pygame.display.update()

pygame.quit()
quit()