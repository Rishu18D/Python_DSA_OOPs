#Bredth First Search
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
visited=[]
queue=[]
def BFS(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=" ")
        
        for next in graph[s]:
            if next not in visited:
                visited.append(next)
                queue.append(next)
BFS(visited,graph,"A")                
    