import re
from geometric import Point
from data import Graph
import config

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
#
# print("Find way")
# weight, min_way = graph.dijkstra()

with open(config.cache_graph, 'r') as file:
    n = int(file.readline())

    for i in range(n):
        arcs = file.readline()
        for arc in arcs.split(";"):
            num1, num2 = arc.split(",")
            num1 = int(num1)
            num2 = float(num2)

            graph.connect(i, num1, num2)

print("Start find way...")
weight, min_way = graph.dijkstra(0, 1)
print("Way is find")
print()

print("Clear")
with open(config.cache_way, "w") as f:
    f.write('')

print("Write to file...")
with open(config.cache_way, "a") as file:
    file.write(str(weight) + "\n")
    file.write(",".join(map(str, min_way)))

print("Write is done")