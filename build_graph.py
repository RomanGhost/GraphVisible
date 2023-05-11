import re
import config
from data import Graph, AVLTree
from geometric import Point, Line, distance_point_to_line, find_lines

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

        id1 = graph.getTopId(p1)
        id2 = graph.getTopId(p2)

        line = Line(p1, p2)
        # заносим сторону фигуры как ребро графа
        graph.connect(id1, id2, line.lenght())
        graph.connect(id2, id1, line.lenght())
        lines.append(line)

    new_line = file.readline()
    for diagonal_str in new_line.split(";"):
        x1, y1, x2, y2 = map(float, re.findall(r"\d+.\d+", diagonal_str))
        diagonals.append(Line(Point(x1, y1), Point(x2, y2)))
        continue

tree = AVLTree()
for num1, p1 in enumerate(graph.tops):
    tree.clear()
    # сортируем точки по углу
    sort_points = sorted(graph.tops, key=lambda it: p1.getAngle(it))
    for p2 in sort_points:
        if p1 is p2:
            continue

        num2 = graph.getTopId(p2)
        line = Line(p1, p2)

        # 1. проверка по отрезкам из дерева, полный перебор из дерева отрезки которые лежат ближе
        collision = tree.collision(line)

        # 2. удалить отрезки, которые лежат левее отрезка р1 - р2 + отрезки, которые имеют смежную точку
        tree.deleteLeft(line)
        tree.deleteAdj(p2)

        # 3. добавить в дерево новые отрезки в которых есть точка p2
        # (при этом надо проверить нет ли этого отрезка в дереве)
        include_lines = find_lines(p2, lines + diagonals)
        for l in include_lines:
            length = distance_point_to_line(p1, l) * (-1 if (l.mid().x - p1.x) < 0 else 1)
            tree.insert(length, l)

        # 4. Если ни один из шагов 1-3 не сработал, то делаем перебор диагоналей и проверяем,
        # не совпадает ли АВ с какой-нибудь диагональю
        if not collision:
            for diagonal in diagonals + lines:
                if line.collision(diagonal):
                    collision = True
                    break

        if not collision:
            graph.connect(num1, num2, line.lenght())

# print("Count tops graph: ", len(graph.tops))
# count_arc = 0
# for arc in graph.connections:
#     count_arc += len(arc)
# print("Count arcs graph: ", count_arc)

arcs_str = ""
for connect in graph.connections:
    for node in connect:
        arcs_str += f"{node.key},{node.weight};"
    arcs_str = arcs_str[:-1] + "\n"

# записываем построенный граф в файл кэша
print("Clear")
with open(config.cache_graph, "w") as f:
    f.write('')

print("Write to file...")
with open(config.cache_graph, "a") as file:
    file.write(str(len(graph.tops)) + "\n")
    file.write(arcs_str)
print("Write is done")

