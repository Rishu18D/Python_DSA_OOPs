def min_cost_path(grid):
    rows, cols = len(grid), len(grid[0])

    # Create a table to store the minimum cost at each cell
    dp = [[0] * cols for _ in range(rows)]

    # Initialize the top-left cell with its cost
    dp[0][0] = grid[0][0]

    # Initialize the first row and first column
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Fill the table in a bottom-up manner
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    # The bottom-right cell contains the minimum cost
    return dp[rows - 1][cols - 1]

# Example usage:
grid = [
    [1, 3, 1],
    [2, 5, 4],
    [6, 8, 2]
]

result = min_cost_path(grid)
print("Minimum cost path:", result)
