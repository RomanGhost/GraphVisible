class ArcNode:
    def __init__(self, key, weight):
        self.key = key
        self.weight = weight


class Graph:
    tops = list()
    size = 0
    connections = list()  # list in list

    def __init__(self):
        self.tops = list()
        self.size = 0
        self.connections = list()

    def addTop(self, top):
        if top in self.tops:
            return

        self.size += 1
        self.tops.append(top)
        self.connections.append(list())

    def getTopId(self, top):
        for num, t in enumerate(self.tops):
            if t == top or t is top:
                return num
        return None

    def connect(self, index: int, index_conn:int, weight):
        if index >= self.size:
            raise IndexError("Idex can't more that size")

        if index < 0:
            raise IndexError("Index can't be negative")

        new_arc = ArcNode(index_conn, weight)
        self.connections[index].append(new_arc)

    def dijkstra(self, from_node: int, to_node: int):
        if from_node >= self.size or to_node >= self.size:
            raise IndexError("Idex can't more that size")

        if from_node < 0 or to_node < 0:
            raise IndexError("Index can't be negative")

        return self. _dijkstra(from_node, to_node)

    def _dijkstra(self, from_node, to_node, prev_weights=0, looks=None, min_way=None):
        """
        рекурсивный поиск кратчайшего пути в графе
        None :return если путь до конечной точки не существует
        list :return кратчайший путь ориентируясь на вес дуги
        """
        if looks is None:
            looks = list()

        if len(looks) == len(self.tops):
            return None

        if min_way is not None and min_way[0] < prev_weights:
            return min_way

        if from_node == to_node:
            if min_way is not None and min_way[0] < prev_weights:
                return min_way
            return prev_weights, looks.copy() + [from_node]

        looks.append(from_node)
        tops = sorted(self.connections[from_node], key=lambda it: (it.weight, it.key))
        for t in tops:
            if t.key in looks:
                continue

            res = self._dijkstra(t.key, to_node, prev_weights+t.weight, looks, min_way)
            if res is not None:
                if min_way is None:
                    min_way = res
                else:
                    if res[0] < min_way[0]:
                        min_way = res
        looks.remove(from_node)
        return min_way

# #  поиск соеденений с точкой
# # сортировка точек по углам для всего множества точек
#
# graph = Graph()
# graph.addTop("Top1")
# graph.addTop("Top2")
# graph.addTop("Top3")
# graph.addTop("Top4")
# graph.addTop("Top5")
# graph.addTop("Top6")
# graph.addTop("Top7")
#
# graph.connect(1-1, 2-1, 1)
# graph.connect(1-1, 5-1, 3)
#
# graph.connect(2-1, 1-1, 1)
# graph.connect(2-1, 3-1, 2)
# graph.connect(2-1, 4-1, 3)
#
# graph.connect(3-1, 2-1, 2)
# graph.connect(3-1, 4-1, 1)
# graph.connect(3-1, 5-1, 1)
#
# graph.connect(4-1, 2-1, 3)
# graph.connect(4-1, 3-1, 1)
# graph.connect(4-1, 5-1, 2)
# graph.connect(4-1, 6-1, 1)
#
# graph.connect(5-1, 1-1, 3)
# graph.connect(5-1, 3-1, 1)
# graph.connect(5-1, 4-1, 2)
# graph.connect(5-1, 6-1, 3)
# graph.connect(5-1, 7-1, 1)
#
# graph.connect(6-1, 4-1, 1)
# graph.connect(6-1, 5-1, 3)
#
# graph.connect(7-1, 5-1, 1)
#
# print("res", graph.dijkstra(0, 6))

