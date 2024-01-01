def dijkstra(graph, start):
    # Create a set to keep track of visited nodes
    visited = set()
    
    # Initialize distances with infinity for all nodes
    distances = {node: float('inf') for node in graph}
    
    # The distance to the start node is 0
    distances[start] = 0
    
    while len(visited) < len(graph):
        # Find the node with the minimum distance
        min_distance_node = None
        for node in graph:
            if node not in visited and (min_distance_node is None or distances[node] < distances[min_distance_node]):
                min_distance_node = node
        
        # Mark the node as visited
        visited.add(min_distance_node)
        
        # Update distances to adjacent nodes
        for neighbor, weight in graph[min_distance_node].items():
            distance = distances[min_distance_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
result = dijkstra(graph, start_node)
print(result)