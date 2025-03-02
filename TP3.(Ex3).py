import numpy as np

class Tree:
    def __init__(self, n, edges):
        self.n = n
        self.adj_list = [[] for _ in range(n + 1)] 
        self.adj_matrix = np.zeros((n, n), dtype=int)
        for u, v in edges:
            self.adj_list[u].append(v)
            self.adj_matrix[u - 1][v - 1] = 1

    def print_adjacency_matrix(self):
        print("Adjacency Matrix:")
        print(self.adj_matrix)

    def inorder_traversal(self, node):
        if not self.adj_list[node]:
            print(node, end=" ")
            return
        if len(self.adj_list[node]) > 0:
            self.inorder_traversal(self.adj_list[node][0])
        print(node, end=" ")
        if len(self.adj_list[node]) > 1:
            self.inorder_traversal(self.adj_list[node][1])

def main():
    edges = [(1,2), (1,3), (2,5), (2,6), (3,4), (4,8), (5,7)]
    n = 8
    tree = Tree(n, edges)
    tree.print_adjacency_matrix()
    x = int(input("Enter node label x: "))
    print(f"Inorder traversal of subtree({x}):")
    tree.inorder_traversal(x)
    print()

if __name__ == "__main__":
    main()
