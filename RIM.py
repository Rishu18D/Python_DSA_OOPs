def is_valid_move(maze, x, y, sol):
    # Check if the move is within the maze boundaries and the cell is not blocked
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1 and sol[x][y] == 0

def solve_maze(maze):
    # Initialize a solution matrix with all cells set to 0
    sol = [[0] * len(maze[0]) for _ in range(len(maze))]

    if solve_maze_util(maze, 0, 0, sol):
        return sol
    else:
        return None

def solve_maze_util(maze, x, y, sol):
    # If the rat reaches the destination, the maze is solved
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        sol[x][y] = 1
        return True

    # Check if the current cell is a valid move 
    if is_valid_move(maze, x, y, sol):
        # Mark the current cell as part of the solution path
        sol[x][y] = 1

        # Move right
        if solve_maze_util(maze, x, y + 1, sol):
            return True

        # Move down
        if solve_maze_util(maze, x + 1, y, sol):
            return True

        # If neither right nor down leads to the solution, backtrack
        sol[x][y] = 0
        return False

# Example usage:
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solution = solve_maze(maze)

if solution:
    print("Solution found:")
    for row in solution:
        print(row)
else:
    print("No solution found.")
