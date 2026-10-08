n = int(input("Enter number of vertices: "))

graph = [[] for _ in range(n)]

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph[u].append(v)
    graph[v].append(u)   # For undirected graph

start = int(input("Enter starting vertex: "))

visited = [False] * n

def dfs(node):
    visited[node] = True
    print(node, end=" ")

    for neighbour in graph[node]:
        if not visited[neighbour]:
            dfs(neighbour)

print("DFS Traversal:")
dfs(start)
