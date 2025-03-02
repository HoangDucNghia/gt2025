import numpy as np

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = np.zeros((vertices, vertices), dtype=int)

    def add_edge(self, u, v, weight):
        self.graph[u - 1][v - 1] = weight
        self.graph[v - 1][u - 1] = weight

    def print_adjacency_matrix(self):
        print("Adjacency Matrix:")
        print(self.graph)

    def prim_mst(self, root):
        selected = [False] * self.V
        selected[root - 1] = True
        mst_edges = []
        total_weight = 0
        for _ in range(self.V - 1):
            min_weight = float('inf')
            x = y = -1
            for i in range(self.V):
                if selected[i]:
                    for j in range(self.V):
                        if not selected[j] and self.graph[i][j]:
                            if min_weight > self.graph[i][j]:
                                min_weight = self.graph[i][j]
                                x, y = i, j
            if x != -1 and y != -1:
                mst_edges.append((x + 1, y + 1, min_weight))
                total_weight += min_weight
                selected[y] = True
        return mst_edges, total_weight

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find_parent(parent, x)
        root_y = self.find_parent(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        edges = []
        for i in range(self.V):
            for j in range(i + 1, self.V):
                if self.graph[i][j] != 0:
                    edges.append((self.graph[i][j], i, j))
        edges.sort()
        parent = list(range(self.V))
        rank = [0] * self.V
        mst_edges = []
        total_weight = 0
        for weight, u, v in edges:
            root_u = self.find_parent(parent, u)
            root_v = self.find_parent(parent, v)
            if root_u != root_v:
                mst_edges.append((u + 1, v + 1, weight))
                total_weight += weight
                self.union(parent, rank, root_u, root_v)
        return mst_edges, total_weight

def main():
    edges = [
        (1, 2, 4), (1, 5, 1), (1, 7, 2), (2, 3, 7), (2, 6, 5),
        (3, 4, 1), (3, 6, 8), (4, 6, 6), (4, 7, 4), (4, 8, 3), 
        (5, 6, 9), (5, 7, 10), (6, 9, 2), (7, 7, 2), (7, 9, 8), (8, 9, 1)
    ]
    n = 9
    graph = Graph(n)
    for u, v, w in edges:
        graph.add_edge(u, v, w)
    graph.print_adjacency_matrix()
    root = int(input("\nEnter root node for Prim's algorithm: "))
    prim_edges, prim_weight = graph.prim_mst(root)
    print("\nPrim's MST Edges:")
    for edge in prim_edges:
        print(edge)
    print("Total weight of Prim's MST:", prim_weight)
    kruskal_edges, kruskal_weight = graph.kruskal_mst()
    print("\nKruskal's MST Edges:")
    for edge in kruskal_edges:
        print(edge)
    print("Total weight of Kruskal's MST:", kruskal_weight)

if __name__ == "__main__":
    main()
