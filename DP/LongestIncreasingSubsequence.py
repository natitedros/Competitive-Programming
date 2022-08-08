class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = {}
        def incSubsequence(ind):
            if ind in dp:
                return dp[ind]
            maxLen = 0
            for i in range(ind+1,l):
                if nums[i] > nums[ind]:
                    maxLen = max(maxLen,incSubsequence(i))
            dp[ind] = 1+maxLen
            return dp[ind]
        mx = 0
        for i in range(l):
            mx = max(mx,incSubsequence(i))
        return mx