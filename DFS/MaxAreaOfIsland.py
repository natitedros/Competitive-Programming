class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        maxSum = 0
        sm = 0
        def findArea(i,j):
            nonlocal m
            nonlocal n
            if i < 0 or i >= m:
                return 0
            if j < 0 or j >= n:
                return 0
            if (i,j) not in visited:
                visited.add((i,j))
            else:
                return 0
            if grid[i][j] == 0:
                return 0
            return 1 + findArea(i-1,j) + findArea(i,j-1) + findArea(i+1,j) + findArea(i,j+1)
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    temp = findArea(i,j)
                    if temp and temp>maxSum:
                        maxSum = temp
        return maxSum