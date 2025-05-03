import uuid
import colorsys

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


class MinHeap:
    def __init__(self):
        self.root = None
        self.total_nodes = 0

    def insert(self, key):
        """
        Inserts a new key into the min heap.
        """
        self.root = self._insert(key, self.root)

    def _insert(self, key, node: Node = None):
        """
        Inserts a new key into the min heap.
        """
        self.total_nodes += 1

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
        """
        Heapifies the min heap up.
        """
        parent, pi = parents[index]
        if parent.val <= node.val:
            return self.root

        parent.val, node.val = node.val, parent.val

        return self._heapify_up(parent, parents, pi)

    def bfs_traverse(self):
        """
        Traverses the min heap in breadth-first order.
        """
        queue = [self.root]
        depth = 0
        while queue:
            current = queue.pop(0)
            current.color = node_color(depth, self.total_nodes)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            depth += 1

    def dfs_traverse(self):
        """
        Traverses the min heap in depth-first order.
        """
        stack = [self.root]
        depth = 0
        while stack:
            current = stack.pop()
            current.color = node_color(depth, self.total_nodes)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            depth += 1


def node_color(depth=0, total_nodes=6):
    """
    Changes the color of the node based on the depth.
    """
    l = 0.5059
    factor = ((1 - l) / total_nodes) * depth
    new_l = min(l + factor, 1)
    new_r, new_g, new_b = colorsys.hls_to_rgb(204 / 360, new_l, 0.881)
    return "#{:02x}{:02x}{:02x}".format(
        int(new_r * 255), int(new_g * 255), int(new_b * 255)
    )


# Min heap
min_heap = MinHeap()
min_heap.insert(0)
min_heap.insert(4)
min_heap.insert(5)
min_heap.insert(10)
min_heap.insert(1)
min_heap.insert(3)

min_heap.dfs_traverse()

draw_tree(min_heap.root)

min_heap.bfs_traverse()

draw_tree(min_heap.root)
