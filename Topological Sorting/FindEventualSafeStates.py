class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outDegree = [0]*n
        incomming = defaultdict(set)
        queue = deque()
        res = []
        for i in range(n):
            if graph[i] == []:
                queue.append(i)
                res.append(i)
            else:
                outDegree[i] = len(graph[i])
                for nodes in graph[i]:
                    incomming[nodes].add(i)
        count = 0
        while queue:
            count += 1
            node = queue.popleft()
            for commers in incomming[node]:
                outDegree[commers] -= 1
                if outDegree[commers] == 0:
                    queue.append(commers)
                    res.append(commers)
        res.sort()
        return res