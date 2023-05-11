class AVLNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None
        self.l = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def getBalance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, key, data):
        self.root = self._insertNode(self.root, AVLNode(key, data))

    def _insertNode(self, node, newNode):
        if node is None:
            return newNode

        if newNode.key < node.key:
            node.left = self._insertNode(node.left, newNode)
        elif newNode.key > node.key:
            node.right = self._insertNode(node.right, newNode)
        else:
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.getBalance(node)

        if balance > 1 and newNode.key < node.left.key:
            return self.rotate_right(node)
        if balance < -1 and newNode.key > node.right.key:
            return self._rotate_left(node)
        if balance > 1 and newNode.key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and newNode.key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def exist(self, key):
        res = self.find(key)
        return res is not None

    def find(self, key):
        return self._findNode(self.root, key)

    def _findNode(self, root, key):
        if root is None:
            return None
        elif key < root.key:
            return self._findNode(root.left, key)
        elif key > root.key:
            return self._findNode(root.right, key)
        else:
            return root

    def minValueNode(self, node):
        currentNode = node
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode

    def delete(self, key):
        self.root = self._deleteNode(self.root, key)

    def _deleteNode(self, node, value):
        if node is None:
            return node

        # Удаление элемента из дерева
        if value < node.key:
            node.left = self._deleteNode(node.left, value)
        elif value > node.key:
            node.right = self._deleteNode(node.right, value)
        else:
            # Удаляем узел с одним или без дочерних узлов
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Удобный случай с узлом, имеющим два дочерних элемента
            temp = self.minValueNode(node.right)
            node.key = temp.key
            node.right = self._deleteNode(node.right, temp.key)

        # Проверка наличия одного или без дочерних элементов
        if node is None:
            return node

        # Обновление высоты текущего узла
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # Вычисление баланс-фактора текущего узла
        balance = self.getBalance(node)

        # Если текущий узел не сбалансирован, выполнение поворотов
        # Влево-влево
        if balance > 1 and self.getBalance(node.left) >= 0:
            return self.rotate_right(node)

        # Вправо-вправо
        if balance < -1 and self.getBalance(node.right) <= 0:
            return self._rotate_left(node)

        # Влево-вправо
        if balance > 1 and self.getBalance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self.rotate_right(node)

        # Вправо-влево
        if balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self._rotate_left(node)

        # Возвращение неизмененного узла (если он уже сбалансирован)
        return node

    def _printNode(self, node, level=0):
        if node is None:
            return

        self._printNode(node.right, level + 1)
        print('\t' * level + f" {node.key} {node.height} [{node.data}]")
        self._printNode(node.left, level + 1)

    def printTree(self):
        self._printNode(self.root)

    def clear(self):
        self._clear(self.root)
        self.root = None

    def _clear(self, node):
        if node:
            self._clear(node.left)
            self._clear(node.right)
            del node

    def count(self):
        return self._countNode(self.root)

    def _countNode(self, node):
        if node is None:
            return 0
        return 1 + self._countNode(node.left) + self._countNode(node.right)

    # внешние функции
    def collision(self, line):
        return self._collisionNode(self.root, line)
    def _collisionNode(self, node, line):
        if node is None:
            return False

        if abs(node.key) < line.lenght():
            if line.collision(node.data):
                return True
            self._collisionNode(node.left, line)
            self._collisionNode(node.right, line)
        return False

    def deleteLeft(self, line):
        return self._deleteLeftNode(self.root, line)

    def _deleteLeftNode(self, node, line):
        if node is None:
            return

        line_x_max = max(line.point1.x, line.point2.x)
        data_x_max = max(node.data.point1.x, node.data.point2.x)
        if line_x_max >= data_x_max:
            self._deleteNode(node, node.key)

        self._deleteLeftNode(node.left, line)
        self._deleteLeftNode(node.right, line)

    def deleteAdj(self, point):
        self._deleteAdjNode(self.root, point)

    def _deleteAdjNode(self, node, point):
        if node is None:
            return

        if point in node.data:
            self._deleteNode(node, node.key)

        self._deleteAdjNode(node.left, point)
        self._deleteAdjNode(node.right, point)