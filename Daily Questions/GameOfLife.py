class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def adder(i,j):
            res = 0
            if i > 0:
                if j > 0:
                    res += board[i-1][j-1]
                res += board[i-1][j]
                if j < n-1:
                    res += board[i-1][j+1]
            if i < m-1:
                if j > 0:
                    res += board[i+1][j-1]
                res += board[i+1][j]
                if j < n-1:
                    res += board[i+1][j+1]
            if j > 0:
                    res += board[i][j-1]
            if j < n-1:
                    res += board[i][j+1]
            return res
        d = {}
        for i in range(m):
            for j in range(n):
                temp = adder(i,j)
                if temp < 2:
                    d[(i,j)] = 0
                elif temp == 3:
                    d[(i,j)] = 1
                elif temp > 3:
                    d[(i,j)] = 0
                else:
                    d[(i,j)] = board[i][j]
        for i in range(m):
            for j in range(n):
                board[i][j] = d[(i,j)]