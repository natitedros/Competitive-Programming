class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left,right = 0,m-1
        mid = 0
        while left<=right:
            mid = left + (right-left)//2
            if matrix[mid][0] < target:
                left = mid+1
            elif matrix[mid][0] > target:
                right = mid-1
            else:
                return True
        row = mid
        if matrix[mid][0] > target:
            row -= 1
        if row < 0:
            return False
        left,right = 0,n-1
        mid = 0
        while left<=right:
            mid = left + (right-left)//2
            if matrix[row][mid]<target:
                left = mid+1
            elif matrix[row][mid]>target:
                right = mid-1
            else:
                return True
        return False
                