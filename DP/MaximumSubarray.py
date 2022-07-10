class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        d = {}
        prev = nums[0]
        res = prev
        for i in range(1,l):
            prev = max(prev+nums[i], nums[i])
            res = max(res, prev)
        return res