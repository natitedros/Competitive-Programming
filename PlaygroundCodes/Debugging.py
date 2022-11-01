from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.vertices = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * self.vertices
        queue = []
        queue.append(s)
        visited[s] = True
        bfs = []
        while queue:
            s = queue.pop(0)
            bfs.append(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)
        return bfs
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(3, 5)

assert g.bfs(0) == [0, 1, 2, 3, 4, 5], "bfs failed"
