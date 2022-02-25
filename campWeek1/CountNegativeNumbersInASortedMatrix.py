class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negatives = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            left = 0
            right = n-1
            while left<=right:
                mid = left + (right-left)//2
                if grid[i][mid] >= 0:
                    left = mid+1
                else:
                    right = mid-1
            if left <= n-1 and grid[i][left] < 0:
                negatives += (n-left)
                
        return negatives