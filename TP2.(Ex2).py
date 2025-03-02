import numpy as np
def build_adjacency_matrix(edges, n):
    matrix = np.zeros((n, n), dtype=int)
    for u, v in edges:
        matrix[u-1][v-1] = 1
    return matrix

def dfs(graph, v, visited, order, n):
    visited[v] = True
    for i in range(n):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited, order, n)
    order.append(v)

def transpose(graph, n):
    transposed = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                transposed[j][i] = 1
    return transposed

def dfs_wcc(graph, v, visited, n):
    visited[v] = True
    for i in range(n):
        if graph[v][i] == 1 and not visited[i]:
            dfs_wcc(graph, i, visited, n)

def find_scc(graph, n):
    visited = [False] * n
    order = []
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, order, n)
    transposed_graph = transpose(graph, n)
    visited = [False] * n
    sccs = []
    for v in reversed(order):
        if not visited[v]:
            scc = []
            dfs_collect(transposed_graph, v, visited, scc, n)
            sccs.append(scc)
    return sccs

def dfs_collect(graph, v, visited, scc, n):
    visited[v] = True
    scc.append(v + 1) 
    for i in range(n):
        if graph[v][i] == 1 and not visited[i]:
            dfs_collect(graph, i, visited, scc, n)

def find_wcc(graph, n):
    undirected_graph = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or graph[j][i] == 1:
                undirected_graph[i][j] = 1
                undirected_graph[j][i] = 1
    visited = [False] * n
    wccs = []
    for v in range(n):
        if not visited[v]:
            wcc = []
            dfs_wcc(undirected_graph, v, visited, n)
            wccs.append([i + 1 for i in range(n) if visited[i] and i not in sum(wccs, [])])
    return wccs

def main():
    edges = [
        (1, 2),
        (1, 4),
        (2, 3),
        (2, 6),
        (5, 4),
        (5, 5),
        (5, 9),
        (6, 3),
        (6, 4),
        (7, 3),
        (7, 5),
        (7, 6),
        (7, 8),
        (8, 3),
        (8, 9),
    ]  
    n = 9
    graph = build_adjacency_matrix(edges, n)
    sccs = find_scc(graph, n)
    print("The number of Strongly Connected Components (SCCs) are:")
    for scc in sccs:
        print(scc)
    wccs = find_wcc(graph, n)
    print("\nThe number of Weakly Connected Components (WCCs) are:")
    for wcc in wccs:
        print(wcc)

main()
