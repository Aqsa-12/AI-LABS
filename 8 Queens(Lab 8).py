import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move="", depth=0, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth  # g(n): path cost so far
        self.cost = cost    # f(n) = g(n) + h(n)

    def __lt__(self, other):
        return self.cost < other.cost

# Heuristic: number of misplaced tiles
def h_misplaced(board, goal):
    return sum([1 for i in range(9) if board[i] != goal[i] and board[i] != 0])

# Generate next states by sliding tiles
def get_neighbors(state):
    neighbors = []
    board = state.board
    zero_index = board.index(0)  
    row, col = divmod(zero_index, 3)

    moves = {
        "Up": (row - 1, col),
        "Down": (row + 1, col),
        "Left": (row, col - 1),
        "Right": (row, col + 1),
    }

    for move, (r, c) in moves.items():
        if 0 <= r < 3 and 0 <= c < 3:
            new_index = r * 3 + c
            new_board = board[:]
            new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
            neighbors.append(PuzzleState(new_board, state, move, state.depth + 1))

    return neighbors

# Reconstruct path from goal state
def reconstruct_path(state):
    path = []
    while state.parent:
        path.append(state.move)
        state = state.parent
    return path[::-1]

# A* Search
def a_star(start, goal):
    open_list = []
    closed_set = set()

    start_state = PuzzleState(start)
    start_state.cost = h_misplaced(start, goal)
    heapq.heappush(open_list, start_state)

    while open_list:
        current = heapq.heappop(open_list)

        if current.board == goal:
            return reconstruct_path(current)

        closed_set.add(tuple(current.board))

        for neighbor in get_neighbors(current):
            if tuple(neighbor.board) in closed_set:
                continue

            g = current.depth + 1
            h = h_misplaced(neighbor.board, goal)
            neighbor.cost = g + h
            heapq.heappush(open_list, neighbor)

    return None


start_state = [1, 2, 3,
               5, 6, 0,
               7, 8, 4] 

goal_state = [1, 2, 3,
              5, 8, 6,
              0, 7, 4]   # goal 

solution = a_star(start_state, goal_state)

print("A* Solution steps:", solution)
print("Number of moves:", len(solution))
