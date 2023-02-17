class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minInd, maxInd = None, None
        left = 0
        res = 0
        for right in range(len(nums)):
            if minK <= nums[right] <= maxK:
                if nums[right] == minK:
                    minInd = right
                if nums[right] == maxK:
                    maxInd = right
                if minInd != None and maxInd != None:
                    res += min(minInd, maxInd) - left + 1
            else:
                left = right + 1
                minInd, maxInd = None, None
        return res