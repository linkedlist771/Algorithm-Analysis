from collections import defaultdict, deque

# 定义图结构
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

# 深度优先搜索 (DFS)
def dfs(graph, v, visited=None):
    if visited is None:
        visited = set()
    visited.add(v)
    print(v, end=' ')
    for neighbour in graph.graph[v]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

# 广度优先搜索 (BFS)
def bfs(graph, v):
    visited = set()
    queue = deque([v])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(neighbour for neighbour in graph.graph[vertex] if neighbour not in visited)

# 示例
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth First Traversal (starting from vertex 2):")
dfs(g, 2)
print("\nBreadth First Traversal (starting from vertex 2):")
bfs(g, 2)
