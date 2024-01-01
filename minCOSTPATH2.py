def min_cost_path_recursive(grid, i, j):
    if i == 0 and j == 0:
        return grid[i][j]
    elif i == 0:
        return min_cost_path_recursive(grid, i, j - 1) + grid[i][j]
    elif j == 0:
        return min_cost_path_recursive(grid, i - 1, j) + grid[i][j]
    else:
        return grid[i][j] + min(
            min_cost_path_recursive(grid, i - 1, j),
            min_cost_path_recursive(grid, i, j - 1),
            min_cost_path_recursive(grid, i - 1, j - 1)
        )

# Example usage:
grid = [
    [1, 3, 1],
    [2, 5, 4],
    [6, 8, 2]
]

rows, cols = len(grid), len(grid[0])
result = min_cost_path_recursive(grid, rows - 1, cols - 1)
print("Minimum cost path:", result)
