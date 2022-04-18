class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        root = {}
        land = {}
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    root[(i,j)] = (i,j)
                    land[(i,j)] = [(i,j)]
        if root == {}:
            return 0
        def find(i, j):
            return root[(i,j)]
        def union(iOne,jOne,iTwo,jTwo):
            rootIOne, rootJOne = find(iOne,jOne)
            rootITwo, rootJTwo = find(iTwo,jTwo)
            if (rootIOne,rootJOne) == (rootITwo,rootJTwo):
                return 0
            if len(land[(rootITwo,rootJTwo)]) > len(land[(rootIOne,rootJOne)]):
                rootIOne, rootITwo = rootITwo, rootIOne
                rootJOne, rootJTwo = rootJTwo, rootJOne
            for i in range(len(land[(rootITwo,rootJTwo)])):
                root[land[(rootITwo,rootJTwo)][i]] = (rootIOne,rootJOne)
                land[(rootIOne,rootJOne)].append(land[(rootITwo,rootJTwo)][i])
            del land[(rootITwo,rootJTwo)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if i>0 and grid[i-1][j] == 1:
                        union(i-1,j,i,j)
                    if j>0 and grid[i][j-1] == 1:
                        union(i,j-1,i,j)
        freq = {}
        for island in root.values():
            if island not in freq:
                freq[island] = 0
            freq[island] += 1
        return max(freq.values())