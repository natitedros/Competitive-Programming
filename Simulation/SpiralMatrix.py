class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        visited = set()
        count = 0
        def isValid(i,j):
            return (0 <= i < m) and (0 <= j < n)
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(i,j,d):
            nonlocal count
            res.append(matrix[i][j])
            count += 1
            visited.add((i,j))
            if count == m*n:
                return
            r,c = dirs[d]
            while (not isValid(i+r,j+c)) or ((i+r,j+c) in visited):
                d = (d+1)%4
                r,c = dirs[d]
            dfs(i+r,j+c,d)
        dfs(0,0,0)
        return res
