class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        neighbor = defaultdict(list)
        for i, (vertex1, vertex2) in enumerate(edges):
            neighbor[vertex1].append([succProb[i], vertex2])
            neighbor[vertex2].append([succProb[i], vertex1])
        queue = list()
        visited = set()
        queue.append([-1 ,start])
        while queue:
            probability, vertex = heapq.heappop(queue)
            visited.add(vertex)
            if vertex == end:
                return -1*probability
            for prob, node in neighbor[vertex]:
                if node not in visited:
                    heapq.heappush(queue, [probability*prob, node])
        return 0
                