class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected) 
        def visitProvince(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] == 1 and  j not in visited:
                    visitProvince(j)
        provinces = 0
        for i in range(n):
            if i not in visited:
                visitProvince(i)
                provinces += 1
        return provinces