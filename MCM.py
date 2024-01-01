def matrix_chain_multiplication(dims):
    n = len(dims) - 1  # Number of matrices in the chain
    memo = {}  # Memoization dictionary

    def helper(i, j):
        if i == j:
            return 0  # Base case: no multiplication needed for a single matrix

        if (i, j) in memo:
            return memo[(i, j)]

        min_cost = float('inf')
        for k in range(i, j):
            cost = helper(i, k) + helper(k + 1, j) + dims[i] * dims[k + 1] * dims[j + 1]
            min_cost = min(min_cost, cost)

        memo[(i, j)] = min_cost
        return min_cost

    return helper(0, n - 1)  # Minimum cost for multiplying matrices from 0 to n-1

# Example usage:
matrix_dimensions = [30, 35, 15, 5, 10, 20, 25]
minimum_scalar_multiplications = matrix_chain_multiplication(matrix_dimensions)
print("Minimum scalar multiplications:", minimum_scalar_multiplications)
