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

    def greedy_best_first(self, start, goal):
        open_list = []
        heapq.heappush(open_list, (self.h[start], start, [start]))
        closed_list = set()

        while open_list:
            h_val, current, path = heapq.heappop(open_list)

            if current == goal:
                return path  # return path only (ignores cost)

            if current in closed_list:
                continue

            closed_list.add(current)

            for neighbor, cost in self.edges.get(current, []):
                if neighbor not in closed_list:
                    heapq.heappush(open_list, (self.h.get(neighbor, float("inf")), neighbor, path + [neighbor]))

        return None
        


graph = Graph()

graph.add_edge("Arad", "Sibiu", 140)
graph.add_edge("Arad", "Timisoara", 118)
graph.add_edge("Arad", "Zerind", 75)
graph.add_edge("Sibiu", "Fagaras", 99)
graph.add_edge("Sibiu", "Rimnicu", 80)
graph.add_edge("Fagaras", "Bucharest", 211)
graph.add_edge("Rimnicu", "Pitesti", 97)
graph.add_edge("Pitesti", "Bucharest", 101)

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

path = graph.greedy_best_first("Arad", "Bucharest")

print("Greedy Best-First path:", path)
