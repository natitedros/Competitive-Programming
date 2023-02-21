class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0]*n
        for u, v in edges:
            indegree[v] += 1
        result = []
        for i in range(n):
            if not indegree[i]:
                result.append(i)
        return result