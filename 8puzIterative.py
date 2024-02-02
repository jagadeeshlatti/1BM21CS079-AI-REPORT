def actions(state):
    # Find the index of the empty tile
    empty_tile_index = state.index(0)
    row, col = divmod(empty_tile_index, 3)  # Convert index to row, column

    possible_actions = []

    # Check if moving tiles up is possible
    if row > 0:
        possible_actions.append('up')

    # Check if moving tiles down is possible
    if row < 2:
        possible_actions.append('down')

    # Check if moving tiles left is possible
    if col > 0:
        possible_actions.append('left')

    # Check if moving tiles right is possible
    if col < 2:
        possible_actions.append('right')

    return possible_actions

def transition(state, action):
    new_state = state.copy()
    empty_tile_index = new_state.index(0)
    row, col = divmod(empty_tile_index, 3)

    # Perform the action by swapping the empty tile with its neighbor
    if action == 'up':
        new_row = row - 1
        new_index = new_row * 3 + col
        new_state[empty_tile_index], new_state[new_index] = new_state[new_index], new_state[empty_tile_index]
    elif action == 'down':
        new_row = row + 1
        new_index = new_row * 3 + col
        new_state[empty_tile_index], new_state[new_index] = new_state[new_index], new_state[empty_tile_index]
    elif action == 'left':
        new_col = col - 1
        new_index = row * 3 + new_col
        new_state[empty_tile_index], new_state[new_index] = new_state[new_index], new_state[empty_tile_index]
    elif action == 'right':
        new_col = col + 1
        new_index = row * 3 + new_col
        new_state[empty_tile_index], new_state[new_index] = new_state[new_index], new_state[empty_tile_index]

    return new_state

def goal_test(state, goal_state):
    return state == goal_state

def depth_limited_search(state, goal_state, limit):
    if goal_test(state, goal_state):
        return [state], []  # Return the solution and actions taken
    elif limit == 0:
        return 'cutoff', []  # Return cutoff and no actions
    else:
        cutoff_occurred = False
        actions_taken = []
        for action in actions(state):
            child_state = transition(state, action)
            result, child_actions = depth_limited_search(child_state, goal_state, limit - 1)
            if result == 'cutoff':
                cutoff_occurred = True
            elif result is not None:
                result.insert(0, state)
                actions_taken = [action] + child_actions
                return result, actions_taken
        return 'cutoff', [] if cutoff_occurred else None

def iterative_deepening_search(initial_state, goal_state):
    depth = 0
    while True:
        result, actions_taken = depth_limited_search(initial_state, goal_state, depth)
        if result != 'cutoff':
            return result, actions_taken
        depth += 1

# Example usage:
initial_state = [1, 2, 3, 4, 5, 0, 6, 7, 8]  # Initial state of the puzzle
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]     # Goal state of the puzzle

solution, actions_taken = iterative_deepening_search(initial_state, goal_state)
if solution is not None:
    print("Solution found:")
    for action, state in zip(actions_taken, solution):
        print("Move:", action)
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()
else:
    print("No solution exists.")
