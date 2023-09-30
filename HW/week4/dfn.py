from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_visit(self, v, parent, visited, dfn, low):
        visited[v] = True
        self.time += 1
        dfn[v] = self.time
        low[v] = self.time

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_visit(neighbor, v, visited, dfn, low)
                low[v] = min(low[v], low[neighbor])
            elif neighbor != parent:
                low[v] = min(low[v], dfn[neighbor])

    def dfnl(self, v):
        visited = {node: False for node in self.graph}
        dfn = {node: None for node in self.graph}
        low = {node: None for node in self.graph}
        self.dfs_visit(v, None, visited, dfn, low)
        return dfn, low


g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'E')
g.add_edge('B', 'C')
g.add_edge('C', 'D')
g.add_edge('C', 'E')
g.add_edge('E', 'F')
g.add_edge('E', 'G')
g.add_edge('F', 'G')

dfn_result, low_result = g.dfnl('A')
print("DFN:", dfn_result)
print("Low:", low_result)
