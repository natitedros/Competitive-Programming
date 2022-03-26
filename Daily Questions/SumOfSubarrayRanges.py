class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        l = len(nums)
        sm = 0
        for i in range(l):
            minVal = nums[i]
            maxVal = nums[i]
            for j in range(i,l):
                if nums[j] > maxVal:
                    maxVal = nums[j]
                if nums[j] < minVal:
                    minVal = nums[j]
                sm += maxVal-minVal
        return sm