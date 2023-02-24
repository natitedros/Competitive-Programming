class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                dp[(i, nums[i] - nums[j])] = max(dp[(i, nums[i] - nums[j])], 1 + dp[(j, nums[i] - nums[j])])
                ans = max(ans, dp[(i, nums[i] - nums[j])])
        return ans + 1