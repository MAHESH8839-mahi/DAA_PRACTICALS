from collections import deque

n = int(input("Enter number of vertices: "))

graph = [[] for _ in range(n)]

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph[u].append(v)
    graph[v].append(u)   
start = int(input("Enter starting vertex: "))

visited = [False] * n
queue = deque()

queue.append(start)
visited[start] = True

print("BFS Traversal:")

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for neighbour in graph[node]:
        if not visited[neighbour]:
            visited[neighbour] = True
            queue.append(neighbour)


