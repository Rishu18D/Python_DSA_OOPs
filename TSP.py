def tsp(graph, n):
    all_points_set = set(range(n))
    memo = {}

    def helper(start, visited_set):
        visited_tuple = tuple(visited_set)
        if (start, visited_tuple) in memo:
            return memo[(start, visited_tuple)]

        if not visited_set:
            return graph[start][0]

        min_cost = float('inf')
        for next_point in visited_set:
            new_set = visited_set - {next_point}
            cost = graph[start][next_point] + helper(next_point, new_set)
            if cost < min_cost:
                min_cost = cost

        memo[(start, visited_tuple)] = min_cost
        return min_cost

    return helper(0, all_points_set)


# Example usage for TSP with a sample graph
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
n = 4
result = tsp(graph, n)
print("Minimum cost for TSP:", result)
