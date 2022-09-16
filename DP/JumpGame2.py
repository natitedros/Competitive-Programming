# Using DP
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(int)
        for i in range(n-2,-1,-1):
            minVal = inf
            for j in range(nums[i],0,-1):
                minVal = min(minVal,dp[i+j])
            dp[i] = 1+minVal
        return dp[0]

# Using Greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        left, right = 0, nums[0]
        jump = 1
        furthest = 0
        while right < n-1:
            temp = 0
            for i in range(left+1,right+1):
                temp = max(temp,i+nums[i])
            left, right = right, temp
            jump += 1
        return jump   