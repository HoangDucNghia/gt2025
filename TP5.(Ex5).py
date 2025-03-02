import heapq

edges = [
    (1,2,9), (1,3,4), (1,6,5), (2,3,7), (2,8,4), (3,4,3), 
    (3,6,1), (4,5,5), (4,6,6), (4,7,2), (5,6,7), (5,9,8),
    (6,8,8), (7,9,4), (8,9,3)
]

graph = {}
for u, v, w in edges:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, w))
    graph[v].append((u, w))

def prim(graph, start=1):
    mst = []
    visited = set()
    pq = [(0, start, -1)]
    
    while pq and len(visited) < len(graph):
        weight, node, parent = heapq.heappop(pq)
        if node not in visited:
            visited.add(node)
            if parent != -1:
                mst.append((parent, node, weight))
            for neighbor, edge_weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, neighbor, node))
    
    return mst

class DisjointSet:
    def __init__(self, n):
        self.parent = {i: i for i in range(1, n+1)}
        self.rank = {i: 0 for i in range(1, n+1)}

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal(edges, n):
    mst = []
    ds = DisjointSet(n)
    edges.sort(key=lambda x: x[2])

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
    return mst

def dijkstra(graph, start, target):
    pq = [] 
    heapq.heappush(pq, (0, start))
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == target:
            break

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    path = []
    node = target
    while node in previous_nodes:
        path.insert(0, node)
        node = previous_nodes[node]
    path.insert(0, start)

    return distances[target], path
n = 9
prim_mst = prim(graph)
kruskal_mst = kruskal(edges, n)
shortest_distance, shortest_path = dijkstra(graph, 1, 9)
print("\nPrim's Algorithm - Minimum Spanning Tree (MST):")
for u, v, w in prim_mst:
    print(f"  {u} -- {w} --> {v}")

print("\nKruskal's Algorithm - Minimum Spanning Tree (MST):")
for u, v, w in kruskal_mst:
    print(f"  {u} -- {w} --> {v}")

print("\nDijkstra's Algorithm - Shortest Path from 1 to 9:")
print(f"  Shortest Distance: {shortest_distance}")
print(f"  Path: {' -> '.join(map(str, shortest_path))}")
