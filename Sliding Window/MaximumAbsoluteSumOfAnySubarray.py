class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        temp1 = nums[0]
        res1 = nums[0]
        for i in range(1,len(nums)):
            temp1 = max(temp1+nums[i],nums[i])
            res1 = max(temp1,res1)
        temp2 = nums[0]
        res2 = nums[0]
        for i in range(1,len(nums)):
            temp2 = min(temp2+nums[i],nums[i])
            res2 = min(temp2,res2)
        return max(abs(res1),abs(res2))