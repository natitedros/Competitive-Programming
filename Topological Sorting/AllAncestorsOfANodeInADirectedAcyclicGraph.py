class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        res = [set() for i in range(n)]
        indegree = [0]*n
        for edge in edges:
            graph[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
            
        q = deque()
        for i in range(n):  
            if not indegree[i]: 
                q.append(i)
        
        while q:
            vertex = q.popleft()
            for val in graph[vertex]:
                res[val].add(vertex)
                for v in res[vertex]:   res[val].add(v)
                indegree[val] -= 1
                if not indegree[val]:   q.append(val)
        for i, val in enumerate(res):
            res[i] = sorted(list(val))
        return res