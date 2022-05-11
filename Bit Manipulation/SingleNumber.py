class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        res = nums[0]
        for i in range(1,l):
            res = res ^ nums[i]
        return res