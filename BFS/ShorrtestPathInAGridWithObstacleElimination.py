class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visited = set()
        q.append((0,0,k,(-1,-1)))
        steps = 0
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def isValid(i,j):
            return 0<=i<m and 0<=j<n
        while q:
            length = len(q)
            while length:
                row,col,bomb,parent = q.popleft()
                length -= 1
                if (row,col,bomb) not in visited:
                    visited.add((row,col,bomb))
                    if bomb < 0:
                        continue
                    if row == m-1 and col == n-1:
                        return steps
                    for r,c in dirs:
                        if isValid(row+r,col+c) and (row+r,col+c) != parent:
                            if grid[row+r][col+c] == 0:
                                q.append((row+r,col+c,bomb,(row,col)))
                            else:
                                q.append((row+r,col+c,bomb-1,(row,col)))
            steps += 1
        return -1