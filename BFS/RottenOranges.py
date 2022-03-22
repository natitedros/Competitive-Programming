class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        visited = {}
        rotten = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
        while rotten:
            q.append([rotten.pop(),0])
            while q:
                (i,j),sec = q.popleft()
                if i<0 or i>m-1:
                    continue
                if j<0 or j>n-1:
                    continue
                if grid[i][j] == 0:
                    continue
                if (i,j) not in visited:
                    visited[(i,j)] = sec
                elif visited[(i,j)] > sec:
                    visited[(i,j)] = sec
                else:
                    continue
                q.append([(i-1,j),sec+1])
                q.append([(i,j-1),sec+1])
                q.append([(i+1,j),sec+1])
                q.append([(i,j+1),sec+1])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    return -1
        if not visited:
            return 0
        return max(visited.values())