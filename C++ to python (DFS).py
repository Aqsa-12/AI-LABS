
from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)

    def addEdge(self, v, w):
        self.adj[v].append(w)   

    # Recursive helper function for DFS
    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.adj[v]:
            if not visited[neighbor]:
                self.DFSUtil(neighbor, visited)

    def DFS(self, v):
        visited = [False] * self.V
        self.DFSUtil(v, visited)

if __name__ == "__main__":

   
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Depth First Traversal (starting from vertex 2):")

    g.DFS(2)
