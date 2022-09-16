class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        d = {}
        recent = n-1
        res = True
        for i in range(n-2,-1,-1):
            res = False
            if i+nums[i] >= n-1 or i+nums[i] >= recent:
                res = True
                recent = i
        return res