class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        minNum = 1
        while minNum in nums:
            minNum += 1
        return minNum