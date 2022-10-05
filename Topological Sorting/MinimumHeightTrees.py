class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        neighbours = defaultdict(set)
        indegree = [0]*n
        for edge in edges:
            neighbours[edge[0]].add(edge[1])
            neighbours[edge[1]].add(edge[0])
            indegree[edge[0]] += 1
            indegree[edge[1]] += 1
        q = deque()
        for i in range(n):
            if indegree[i] == 1:
                q.append(i)
        nodesLeft = n
        while nodesLeft > 2:
            count = len(q)
            for i in range(count):
                node = q.popleft()
                for nd in neighbours[node]:
                    indegree[nd] -= 1
                    if indegree[nd] == 1:
                        q.append(nd)
            nodesLeft -= count
        return q
            