class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0]) 
        dp = {}
        def isValid(i,j):
            return (i < m) and (j < n) and (obstacleGrid[i][j] == 0)
        directions = [(1,0),(0,1)]
        
        def dfs(row, col):
            if (row,col) in dp:
                return dp[(row,col)]
            if row == m-1 and col == n-1 and obstacleGrid[row][col] == 0:
                return 1
            elif isValid(row, col):
                paths = 0
                for a,b in directions:
                    new_row = row + a
                    new_col = col + b
                    paths += dfs(new_row,new_col)
                dp[(row,col)] = paths
                return dp[(row,col)]
            else:
                dp[(row,col)] = 0
                return 0
        return dfs(0,0)