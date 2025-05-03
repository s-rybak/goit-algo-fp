import networkx as nx
import heapq

G = nx.Graph()

G.add_edge("A", "B", weight=5)
G.add_edge("A", "C", weight=10)
G.add_edge("B", "D", weight=3)
G.add_edge("C", "D", weight=2)
G.add_edge("D", "E", weight=4)


def dijkstra_heap(graph, start):
    """Dijkstra's algorithm with binary heap"""
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    paths = {vertex: [] for vertex in graph}
    paths[start] = [start]

    while priority_queue:

        current_distance, vertex = heapq.heappop(priority_queue)

        if current_distance > distances[vertex]:
            continue

        for neighbor, edge in graph[vertex].items():
            weight = edge["weight"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[vertex] + [neighbor]
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, paths


print("\nРезультат алгоритму Дейкстри з бінарною купою:")
distances, paths = dijkstra_heap(G, "A")
print("Відстані:", distances)
print("Шляхи:", paths)
