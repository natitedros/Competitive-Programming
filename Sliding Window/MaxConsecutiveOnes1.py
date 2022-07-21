class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left,right,res = 0,0,0
        while right < len(nums):
            if nums[right] == 0:
                left = right+1
            res = max(res,right-left+1)
            right += 1
        return res