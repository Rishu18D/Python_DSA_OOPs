import heapq

def dijkstra(graph, start):
    # Initialize distances and predecessors
    distances = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    distances[start] = 0
    
    # Priority queue to store nodes with their tentative distances
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Get the node with the smallest tentative distance
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we've already visited this node, skip it
        if current_distance > distances[current_node]:
            continue
        
        # Update the distances to neighbors through the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If this path is shorter than the current shortest path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, predecessors

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances, predecessors = dijkstra(graph, start_node)

# Print the shortest distances and paths from the start node
for node in graph:
    if distances[node] == float('inf'):
        print(f"Node {node}: Unreachable")
    else:
        path = []
        current_node = node
        while current_node is not None:
            path.insert(0, current_node)
            current_node = predecessors[current_node]
        print(f"Node {node}: Shortest Distance = {distances[node]}, Path = {' -> '.join(path)}")
