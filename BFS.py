graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = set() # Set to keep track of visited nodes.
queue = []
def dfs(visited,graph,node):
    queue.append(node) #Enqueue
    while queue:
        #Dequeue
        n = queue.pop(0)
        print(n)
        for neighbour in graph[n]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
dfs(visited,graph,'A')
