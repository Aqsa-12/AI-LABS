# Graph class
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

# DFS using stack
def dfs_stack(graph, start, goal):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            print(node, end=" ")

            if node == goal:
                print("\nGoal node found!")
                return visited

            # Push children in reverse order so left-most is visited first
            if node in graph:
                stack.extend(reversed(graph[node]))

    print("\nGoal node not found!")
    return visited

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'F')
g.add_edge('A', 'D')
g.add_edge('A', 'E')
g.add_edge('B', 'K')
g.add_edge('B', 'J')
g.add_edge('K', 'N')
g.add_edge('K', 'M')
g.add_edge('D', 'G')
g.add_edge('E', 'C')
g.add_edge('E', 'H')
g.add_edge('E', 'I')
g.add_edge('I', 'L')

# Run DFS from A to G
path = dfs_stack(g.graph, 'A', 'G')
print("DFS Path Traversed:", path)
