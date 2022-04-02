class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = {}
        def pathSum(i,j):
            if i>=m or j>=n:
                return 0
            if (i,j) not in dp:
                if i < m-1 and j < n-1:
                    dp[(i,j)] = grid[i][j]+min(pathSum(i+1,j),pathSum(i,j+1))
                elif i < m-1:
                    dp[(i,j)] = grid[i][j]+pathSum(i+1,j)
                elif j < n-1:
                    dp[(i,j)] = grid[i][j]+pathSum(i,j+1)
                else:
                    dp[(i,j)] = grid[i][j]
            return dp[(i,j)]
        return pathSum(0,0)