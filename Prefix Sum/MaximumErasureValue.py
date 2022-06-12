class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = len(nums)
        unique = set()
        left = -1
        right = 0
        subarraySum = 0
        maxSum = 0
        while right < l:
            if nums[right] not in unique:
                unique.add(nums[right])
                subarraySum += nums[right]
                right += 1
            else:
                left += 1
                unique.discard(nums[left])
                subarraySum -= nums[left]
            maxSum = max(maxSum, subarraySum)
        return maxSum