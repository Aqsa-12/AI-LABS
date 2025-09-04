import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.h = {}   # heuristic values (h(n))

    def add_edge(self, node, neighbor, cost):
        if node not in self.edges:
            self.edges[node] = []
        self.edges[node].append((neighbor, cost))

    def set_heuristic(self, h_values):
        self.h = h_values

    def a_star(self, start, goal):
        open_list = []
        heapq.heappush(open_list, (self.h[start], 0, start, [start]))  
        closed_list = set()

        while open_list:
            f, g, current, path = heapq.heappop(open_list)

            if current == goal:
                return path, g  # return path and total cost

            if current in closed_list:
                continue

            closed_list.add(current)

            for neighbor, cost in self.edges.get(current, []):
                if neighbor not in closed_list:
                    g_new = g + cost
                    f_new = g_new + self.h.get(neighbor, float("inf"))
                    heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

        return None, float("inf")
    

# -------------------------------
# Example graph (Romania Map snippet)
# -------------------------------
graph = Graph()

# Define edges (like from Arad example)
graph.add_edge("Arad", "Sibiu", 140)
graph.add_edge("Arad", "Timisoara", 118)
graph.add_edge("Arad", "Zerind", 75)
graph.add_edge("Sibiu", "Fagaras", 99)
graph.add_edge("Sibiu", "Rimnicu", 80)
graph.add_edge("Fagaras", "Bucharest", 211)
graph.add_edge("Rimnicu", "Pitesti", 97)
graph.add_edge("Pitesti", "Bucharest", 101)

# Straight-line heuristics to Bucharest
heuristics = {
    "Arad": 366,
    "Sibiu": 253,
    "Timisoara": 329,
    "Zerind": 374,
    "Fagaras": 176,
    "Rimnicu": 193,
    "Pitesti": 100,
    "Bucharest": 0
}

graph.set_heuristic(heuristics)

# Run A* from Arad → Bucharest
path, cost = graph.a_star("Arad", "Bucharest")

print("Best path:", path)
print("Total cost:", cost)
