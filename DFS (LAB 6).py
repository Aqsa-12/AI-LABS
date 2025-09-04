# Graph class using adjacency list
class Graph:
    def __init__(self):
        self.adj = {}   # adjacency list dictionary

    def add_edge(self, u, v):
        # If u is not already in adj list, create empty list
        if u not in self.adj:
            self.adj[u] = []
        # If v is not already in adj list, create empty list
        if v not in self.adj:
            self.adj[v] = []
        # Add v to u's adjacency list
        self.adj[u].append(v)

    # Recursive DFS
    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in self.adj[node]:
                self.dfs(neighbor, visited)



g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 7)
g.add_edge(1, 8)
g.add_edge(2, 3)
g.add_edge(2, 6)
g.add_edge(3, 4)
g.add_edge(3, 5)
g.add_edge(8, 9)
g.add_edge(8, 12)
g.add_edge(9, 10)
g.add_edge(9, 11)


print("DFS Traversal:")
g.dfs(1)