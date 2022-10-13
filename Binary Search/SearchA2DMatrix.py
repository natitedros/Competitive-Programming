class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = [0,0]
        right = [m-1,n-1]
        # while left <= right:
        i = 10
        while i:
            print(left,right)
            mid = [0,0]
            mid[0] = (left[0]+right[0])//2
            mid[1] = ((left[1]+(left[0]*n)+right[1]+(right[0]*n))//2)%n
            if matrix[mid[0]][mid[1]] < target:
                left = [mid[0],(mid[1]+1)%n]
                if left[1] == 0:
                    left[0] += 1
            elif matrix[mid[0]][mid[1]] > target:
                right = [mid[0],(mid[1]-1)%n]
                if right[1] == n-1:
                    right[0] -= 1
            else:
                return True
            i -= 1
        return False
                