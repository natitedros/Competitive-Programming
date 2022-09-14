class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = defaultdict(list)
        dp2 = defaultdict(list)
        dp1[n-1] = [nums[n-1],0]
        dp1[n-2] = [nums[n-2],n-1]
        for i in range(n-3,-1,-1):
            temp = 0
            lvl = i
            for j in range(i+2,n):
                if dp1[j][1] != i:
                    temp = max(temp,dp1[j][0])
                    lvl = dp1[j][1]
            dp1[i] = [temp+nums[i],lvl]
        dp2[0] = [nums[0],n-1]
        dp2[1] = [nums[1],0]
        for i in range(2,n):
            temp = 0
            lvl = i
            for j in range(i-2,-1,-1):
                if dp2[j][1] != i:
                    temp = max(temp,dp2[j][0])
                    lvl = dp2[j][1]
            dp2[i] = [temp+nums[i],lvl]
        return max(max(dp1.values())[0],max(dp2.values())[0])
        