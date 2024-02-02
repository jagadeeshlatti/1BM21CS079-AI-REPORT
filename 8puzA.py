import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, depth=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = self.depth + self.heuristic()

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def heuristic(self):
        # Manhattan distance heuristic
        h = 0
        goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != goal_state[i][j]:
                    target_value = self.state[i][j]
                    target_i, target_j = divmod(target_value, 3)
                    h += abs(i - target_i) + abs(j - target_j)
        return h

    def get_neighbors(self):
        neighbors = []
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in moves:
            new_state = [row[:] for row in self.state]
            i, j = self.find_empty()
            new_i, new_j = i + dx, j + dy
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                neighbors.append(PuzzleNode(new_state, parent=self, move=(dx, dy), depth=self.depth + 1))
        return neighbors

    def find_empty(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def get_solution(self):
        solution = []
        node = self
        while node.parent is not None:
            solution.append(node.move)
            solution.append(node.state)  # Append the state after the move
            node = node.parent
        solution.reverse()
        return solution

def print_board(state):
    for row in state:
        print(row)
    print()

def solve_8_puzzle(initial_state):
    start_node = PuzzleNode(initial_state)
    open_set = [start_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)
        if current_node.state == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            return current_node.get_solution()
        closed_set.add(current_node)

        for neighbor in current_node.get_neighbors():
            if neighbor in closed_set:
                continue
            if neighbor not in open_set or neighbor.cost < open_set[open_set.index(neighbor)].cost:
                heapq.heappush(open_set, neighbor)
                print_board(neighbor.state)  # Print the board state after the move
                print("Move:", neighbor.move)  # Print the move made

    return None

# Example usage:
initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
solution = solve_8_puzzle(initial_state)
if solution:
    print("Solution found in", len(solution) // 2, "moves:")
else:
    print("No solution found.")
