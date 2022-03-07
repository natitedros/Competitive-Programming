class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = set()
        def dfs(i,j):
            if i < 0 or i>m-1:
                return 0
            if j < 0 or j>n-1:
                return 0
            if board[i][j] == "O" and (i,j) not in visited:
                visited.add((i,j))
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i,j+1)  
        for i in range(m):
            if board[i][0] == "O" and (i,0) not in visited:
                dfs(i,0)
            if board[i][n-1] == "O" and (i,n-1) not in visited:
                dfs(i,n-1)
        for j in range(n):
            if board[0][j] == "O" and (0,j) not in visited:
                dfs(0,j)
            if board[m-1][j] == "O" and (m-1,j) not in visited:
                dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    board[i][j] = "X"