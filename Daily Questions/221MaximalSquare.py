class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}
        maxVal = 0
        def isValid(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and matrix[row][col] == "1"
        dirs = [(1, 0), (0, 1), (1, 1)]
        def rec(row, col):
            nonlocal maxVal
            if (row, col) in dp:
                return dp[(row, col)]
            if not isValid(row, col):
                dp[(row, col)] = 0
                return 0
            temp = inf
            for r, c in dirs:
                newR, newC = row+r, col+c
                temp = min(temp, rec(newR, newC))
            dp[(row, col)] = temp + 1
            maxVal = max(maxVal, dp[(row, col)])
            return dp[(row, col)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                rec(i ,j)
        return maxVal**2