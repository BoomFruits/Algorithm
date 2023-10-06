graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = set() # Set to keep track of visited nodes.
def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            # Recusion 1: 'A' => neighbour = 'B' 
            # Recusion 2: 'B' => neighbour = 'D'
            # Recusion 3: 'B' => neighbour = 'E'
            # Recusion 4: 'E' => neighbour = 'F'
            # Recusion 5: 'A' => neighbour = 'C'
            dfs(visited,graph,neighbour)
dfs(visited,graph,'A')