function VacuumCleanerAlgorithm():
    Initialize environment with multiple rooms
    Place vacuum cleaner in the starting position of the first room
   
    current_room = first_room
   
    while True:
        Perceive current cell state
        if CurrentCell is dirty:
            Clean CurrentCell
        else:
            if There are adjacent dirty cells:
                Move to one of the adjacent dirty cells
            else:
                Choose a direction to move (e.g., randomly)
                while ChosenDirection is blocked by an obstacle or out of bounds:
                    Choose a new direction to move
                Move in the chosen direction
       
        if All cells in current room are clean:
            if current_room is not last_room:
                Move to the entrance of the next room
                current_room = next_room
            else:
                if All rooms are clean or stopping condition is met:
                    break
