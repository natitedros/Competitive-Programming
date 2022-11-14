class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        path = set()
        for a, b in connections:
            path.add((a, b))
            neighbors[a].append(b)
            neighbors[b].append(a)
        visited = set()
        change = 0
        def dfs(city):
            nonlocal change
            visited.add(city)
            for neigh in neighbors[city]:
                if neigh not in visited:
                    if (city, neigh) in path:
                        change += 1
                    dfs(neigh)
        dfs(0)
        return change
        