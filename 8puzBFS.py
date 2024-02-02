from collections import deque

# Represents the 8-puzzle problem
class Puzzle:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        self.actions = [self.move_up, self.move_down, self.move_left, self.move_right]

    # Move the empty tile up
    def move_up(self, state):
        new_state = state[:]
        index = new_state.index(0)
        if index not in [0, 1, 2]:
            new_state[index], new_state[index - 3] = new_state[index - 3], new_state[index]
            return new_state
        else:
            return None

    # Move the empty tile down
    def move_down(self, state):
        new_state = state[:]
        index = new_state.index(0)
        if index not in [6, 7, 8]:
            new_state[index], new_state[index + 3] = new_state[index + 3], new_state[index]
            return new_state
        else:
            return None

    # Move the empty tile left
    def move_left(self, state):
        new_state = state[:]
        index = new_state.index(0)
        if index not in [0, 3, 6]:
            new_state[index], new_state[index - 1] = new_state[index - 1], new_state[index]
            return new_state
        else:
            return None

    # Move the empty tile right
    def move_right(self, state):
        new_state = state[:]
        index = new_state.index(0)
        if index not in [2, 5, 8]:
            new_state[index], new_state[index + 1] = new_state[index + 1], new_state[index]
            return new_state
        else:
            return None

    # Solve the puzzle using BFS
    def solve(self):
        visited = set()
        queue = deque([(self.initial_state, [])])

        while queue:
            state, path = queue.popleft()
            if state == self.goal_state:
                return path
            visited.add(tuple(state))

            for action in self.actions:
                new_state = action(state)
                if new_state and tuple(new_state) not in visited:
                    print("Move:", action.__name__[5:])
                    self.print_board(new_state)
                    queue.append((new_state, path + [action.__name__[5:]]))
        return None

    # Function to print the board
    def print_board(self, state):
        for i in range(0, 9, 3):
            print(state[i:i+3])

# Example usage
if __name__ == "__main__":
    initial_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]  # Example initial state
    puzzle = Puzzle(initial_state)
    solution = puzzle.solve()

    if solution:
        print("Solution found in {} moves:".format(len(solution)))
        for i, step in enumerate(solution, 1):
            print("Step {}: {}".format(i, step))
    else:
        print("No solution found.")
