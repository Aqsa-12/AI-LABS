

graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'K': ['N', 'M'],
    'D': ['G'],
    'E': ['C', 'H', 'I'],
    'I': ['L'],
    'F': [],
    'J': [],
    'N': [],
    'M': [],
    'G': [],
    'C': [],
    'H': [],
    'L': []
}

def DLS(node, goal, limit):
    if node == goal:
        return True
    if limit <= 0:
        return False
    for child in graph[node]:
        if DLS(child, goal, limit - 1):
            return True
    return False

def IDDFS(start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nSearching at depth: {depth}")
        if DLS(start, goal, depth):
            return True
    return False

start, goal = 'A', 'G'
max_depth = 5
found = IDDFS(start, goal, max_depth)
print(f"\nFound {goal} within depth {max_depth}? {found}")
# Depth Limited Search (DLS) helper with path tracking
def depth_limited_search(start, goal, depth, graph, path):
    path.append(start)  # add current node to path

    if start == goal:
        return True

    if depth <= 0:
        path.pop()
        return False

    for neighbor in graph.get(start, []):
        if depth_limited_search(neighbor, goal, depth - 1, graph, path):
            return True

    path.pop()
    return False


def iddfs(start, goal, max_depth, graph):
    for depth in range(max_depth + 1):
        path = []
        print(f"🔍 Searching at depth {depth}...")
        if depth_limited_search(start, goal, depth, graph, path):
            print(f"✅ Goal '{goal}' found at depth {depth}")
            print("➡ Path:", " → ".join(path))
            return True
    print("❌ Goal not found within depth limit")
    return False


tree = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'K': ['N', 'M'],
    'J': [],
    'N': [],
    'M': [],
    'F': [],
    'D': ['G'],
    'G': [],
    'E': ['C', 'H', 'I'],
    'C': [],
    'H': [],
    'I': ['L'],
    'L': []
}

start_node = 'A'
goal_node = 'G'
max_depth = 5

iddfs(start_node, goal_node, max_depth, tree)

