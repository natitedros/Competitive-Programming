class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def isValid(i,j):
            return 0<=i<n and 0<=j<n
        directions =[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        q = deque()
        if grid[0][0] == 0: 
            q.append((0,0,1))
        visited = set()
        visited.add((0,0))
        while q:
            row,col,level = q.popleft()
            if row == n-1 and col == n-1:
                return level
            for a,b in directions:
                new_row = row + a
                new_col = col + b
                if isValid(new_row,new_col) and (new_row,new_col) not in visited:
                    visited.add((new_row,new_col))
                    if grid[new_row][new_col] == 0:
                        q.append((new_row,new_col,level+1))
        return -1