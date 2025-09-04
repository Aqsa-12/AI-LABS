# Depth Limited Search implementation

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
    print(f"Visiting: {node}, Depth limit: {limit}")
    if node == goal:
        return True
    if limit <= 0:
        return False
    for child in graph[node]:
        if DLS(child, goal, limit - 1):
            return True
    return False

# Test Depth Limited Search
start, goal = 'A', 'G'
limit = 2
found = DLS(start, goal, limit)
print(f"\nFound {goal} within depth {limit}? {found}")
