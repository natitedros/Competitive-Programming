class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0]*n
        for i in range(n-1,-1,-1):
            if i == n-1:
                arr[i] = 1
            elif i == n-2:
                arr[i] = 2
            else:
                arr[i] = arr[i+1]+arr[i+2]
        return arr[0]