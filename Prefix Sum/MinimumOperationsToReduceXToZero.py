class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        l = len(nums)
        sm = sum(nums)
        required = sm - x
        left = -1
        right = 0
        subarraySum = 0
        maxLen = 0
        isFound = False
        while right < l:
            subarraySum += nums[right]
            while left < right and subarraySum > required:
                left += 1
                subarraySum -= nums[left]
            if subarraySum == required:
                isFound = True
                maxLen = max(maxLen,right-left)
            right += 1
        if not isFound:
            return -1
        return l-maxLen