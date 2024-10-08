import heapq
import copy

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def manhattan_distance(state):
    distance = 0
    for i in range(4):
        for j in range(4):
            if state[i][j] != 0:
                row, col = divmod(state[i][j] - 1, 4)
                distance += abs(i - row) + abs(j - col)
    return distance

def get_neighbors(node):
    neighbors = []
    i, j = next((i, j) for i, row in enumerate(node.state) for j, value in enumerate(row) if value == 0)
    
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    
    for move in moves:
        new_i, new_j = i + move[0], j + move[1]
        if 0 <= new_i < 4 and 0 <= new_j < 4:
            new_state = copy.deepcopy(node.state)
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            neighbors.append(PuzzleNode(new_state, node, move, node.cost + 1, manhattan_distance(new_state)))
    
    return neighbors

def a_star(initial_state, goal_state):
    initial_node = PuzzleNode(initial_state, None, None, 0, manhattan_distance(initial_state))
    goal_node = PuzzleNode(goal_state)

    open_set = [initial_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_node.state:
            path = []
            while current_node.parent:
                path.append(current_node.move)
                current_node = current_node.parent
            path.reverse()
            return path

        closed_set.add(tuple(map(tuple, current_node.state)))

        neighbors = get_neighbors(current_node)
        for neighbor in neighbors:
            if tuple(map(tuple, neighbor.state)) not in closed_set:
                heapq.heappush(open_set, neighbor)

    return None

if __name__ == "__main__":
    # Example Usage:
    initial_state = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

    goal_state = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]

    solution = a_star(initial_state, goal_state)
    print("Solution:", solution)
