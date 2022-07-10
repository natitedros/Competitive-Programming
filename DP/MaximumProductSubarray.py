class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        prevMax = nums[0]
        prevMin = nums[0]
        res = nums[0]
        for i in range(1,l):
            if nums[i] < 0:
                prevMax, prevMin = max(prevMin*nums[i], nums[i]), min(prevMax*nums[i], nums[i])
            else:
                prevMax, prevMin = max(prevMax*nums[i], nums[i]), min(prevMin*nums[i], nums[i])
            res = max(res, prevMax)
        return res