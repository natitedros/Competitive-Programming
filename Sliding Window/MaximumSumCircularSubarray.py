class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        temp = max(nums)
        if temp <= 0:
            return temp
        res1 = temp1 = temp2 = res2 = nums[0]
        for i in range(1,n):
            temp1 = max(temp1+nums[i],nums[i])
            temp2 = min(temp2+nums[i],nums[i])
            res1 = max(res1,temp1)
            res2 = min(res2,temp2)
        return max(res1, sum(nums) - res2)