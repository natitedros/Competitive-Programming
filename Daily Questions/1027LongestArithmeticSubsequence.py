class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        def rec(ind, diff, prev):
            if (ind, diff, prev) in dp:
                return dp[(ind, diff, prev)]

            if ind == len(nums):
                return 0

            dp[(ind, diff, prev)] = rec(ind+1, diff, prev)
            if prev == -2000:
                dp[(ind, diff, prev)] = max(dp[(ind, diff, prev)], 1 + rec(ind+1, diff, nums[ind]))
            elif diff == -2000 or nums[ind] - prev == diff:
                
                dp[(ind, diff, prev)] = max(dp[(ind, diff, prev)], 1 + rec(ind+1, nums[ind] - prev, nums[ind]))

            return dp[(ind, diff, prev)]
        return rec(0, -2000, -2000)