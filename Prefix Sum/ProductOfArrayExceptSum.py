class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        leftMul = 1
        rightMul = 1
        res = [1]*l
        for i in range(l):
            res[i] *= leftMul
            res[-1-i] *= rightMul
            leftMul *= nums[i]
            rightMul *= nums[-1-i]
        return res