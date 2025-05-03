import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла
        self.height = 1


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(
            node.id, color=node.color, label=node.val
        )  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {
        node[0]: node[1]["label"] for node in tree.nodes(data=True)
    }  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node: Node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node: Node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z: Node):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, y: Node):
        x = y.left
        T3 = x.right

        x.right = y
        y.left = T3

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def min_value_node(self, node: Node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def insert(self, key):
        self.root = self._insert(key, self.root)

    def _insert(self, key, node):
        if not node:
            return Node(key)

        if key < node.val:
            node.left = self._insert(key, node.left)
        elif key > node.val:
            node.right = self._insert(key, node.right)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        if balance > 1:
            if key < node.left.val:
                return self.right_rotate(node)
            else:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

        if balance < -1:
            if key > node.right.val:
                return self.left_rotate(node)
            else:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

        return node


class MinHeap:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(key, self.root)

    def _insert(self, key, node: Node = None):
        if not node:
            self.root = Node(key)
            return self.root

        queue = [(node, None)]
        i = 0
        while queue:
            current, _ = queue[i]  # used i in order to keep path to current node

            if not current.left:
                current.left = Node(key)
                return self._heapify_up(current.left, queue, i)
            elif not current.right:
                current.right = Node(key)
                return self._heapify_up(current.right, queue, i)

            queue.append((current.left, i))
            queue.append((current.right, i))
            i += 1

    def _heapify_up(self, node, parents, index):
        parent, pi = parents[index]
        if parent.val <= node.val:
            return self.root

        parent.val, node.val = node.val, parent.val

        return self._heapify_up(parent, parents, pi)


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
# draw_tree(root)

# AVL tree
# Додав ще AVL tree бо не до кінця зрозумів яке саме дерево хочуть бачити
avl_tree = AVLTree()
avl_tree.insert(0)
avl_tree.insert(4)
avl_tree.insert(5)
avl_tree.insert(10)
avl_tree.insert(1)
avl_tree.insert(3)

# draw_tree(avl_tree.root)


# Min heap
min_heap = MinHeap()
min_heap.insert(0)
min_heap.insert(4)
min_heap.insert(5)
min_heap.insert(10)
min_heap.insert(1)
min_heap.insert(3)

draw_tree(min_heap.root)
