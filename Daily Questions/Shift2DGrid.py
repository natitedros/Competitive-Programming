class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        row = m
        col = n
        step = k
        rotated = []
        if k == m*n:
            return grid
        elif k > m*n:
            while step>=m*n:
                step -= m*n
        while step and row > 0:
            row -= 1
            col = n
            while col > 0 and step:
                step -= 1
                col -= 1
                rotated.append(grid[row][col])
        shifted = []
        flag = True
        i = 0
        while i < m and flag:
            j = 0
            while j < n and flag:
                if i == row and j == col:
                    flag = False
                else:
                    shifted.append(grid[i][j])
                j+=1
            i+=1
        res = [[0 for x in range(n)] for y in range(m)]
        shifted.reverse()
        i = 0
        while i < m:
            j = 0
            while j < n:
                if rotated:
                    res[i][j] = rotated.pop()
                elif shifted:
                    res[i][j] = shifted.pop()
                j+=1
            i+=1
        return res