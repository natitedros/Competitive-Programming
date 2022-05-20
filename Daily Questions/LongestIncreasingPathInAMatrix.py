class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        m = len(matrix)
        n = len(matrix[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def isValid(row,col):
            return (0 <= row < m) and (0 <= col < n)
        def findLength(row, col):
            if (row,col) in dp:
                return dp[(row,col)]
            maxLen = 1
            for a,b in directions:
                new_row = row+a
                new_col = col+b
                if isValid(new_row, new_col) and matrix[new_row][new_col] > matrix[row][col]:
                    maxLen = max(maxLen,findLength(new_row, new_col) + 1)
            dp[(row, col)] = maxLen
            return dp[(row,col)]
        maxLength = 0
        for i in range(m):
            for j in range(n):
                maxLength = max(findLength(i,j), maxLength)
        return maxLength