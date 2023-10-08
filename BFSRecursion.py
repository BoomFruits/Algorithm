graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = set()
queue = []
def BFS(visited,graph,queue):
    if(len(queue) == 0):
        return
    node = queue.pop(0)
    print(node)
    for neighbour in graph[node]:
        if(neighbour not in visited):
            queue.append(neighbour)
            visited.add(neighbour)
    BFS(visited,graph,queue)
BFS(visited,graph,['A'])
        