class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guarded = set()
        guards = set((r,c) for r,c in guards)
        walls = set((r,c) for r,c in walls)
        def isValid(i,j):
            return 0 <= i < m and 0 <= j < n
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        def dfs(i, j, direction):
            row, col = directions[direction]
            newRow = i+row
            newCol = j+col
            if not isValid(newRow, newCol) or (newRow, newCol) in walls or (newRow, newCol) in guards:
                return 0
            if (newRow, newCol) not in guarded:
                guarded.add((newRow, newCol))
            dfs(newRow, newCol, direction)
        for row, col in guards:
            for i in range(0,4):
                dfs(row, col, i)
        return (m*n) - (len(guards)+len(walls)+len(guarded))