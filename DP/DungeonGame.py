class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        dp = defaultdict(int)
        def isValid(i,j):
            return 0<=i<m and 0<=j<n
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                temp = 0
                if isValid(i+1,j) and isValid(i,j+1):
                    temp = min(0,dungeon[i][j]+max(dp[(i+1,j)],dp[(i,j+1)]))
                else:
                    temp = min(0,dungeon[i][j]+(dp[(i+1,j)]+dp[(i,j+1)]))
                dp[(i,j)] = temp
        return abs(dp[(0,0)])+1
                               