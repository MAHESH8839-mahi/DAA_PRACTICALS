from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])


graph = {
    0: [1, 5],
    1: [2, 4],
    2: [3],
    3: [],
    4: [],
    5: []
}

bfs(graph, 0)

