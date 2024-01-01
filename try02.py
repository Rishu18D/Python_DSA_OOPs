def dijkstra(graph,start):
    visited=set()
    distances={node:float('inf') for node in graph}
    distances[start]=0
    while len(visited)<len(graph):
        min_distance_node=None
        for node in graph:
            if node not in visited and(min_distance_node is None or distances[node]<distances[min_distance_node]):
                min_distance_node=node
        visited.add(min_distance_node)
        for aage, weight in graph[min_distance_node].items():
           distance=distances[min_distance_node]+weight
           if distance<distances[aage]:
                distances[aage]=distance
    return distances            
graph={
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_node="A"
result=dijkstra(graph,start_node)
print(result)                   