class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,right,sm,res = 0,0,0,inf
        while right < len(nums):
            sm += nums[right]
            while sm >= target:
                res = min(res,right-left+1)
                sm -= nums[left]
                left += 1
            right += 1
        if res == inf:
            return 0
        return res