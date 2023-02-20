class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minVal = nums[0]
        diff = -inf
        for i in range(1, len(nums)):
            diff = max(diff, nums[i] - minVal)
            minVal = min(minVal, nums[i])
            print(diff)
        return diff if diff > 0 else -1