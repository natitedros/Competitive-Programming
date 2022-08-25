class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        ind = 0
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                count += 1
                ind = i
        if count == 0:
            return True
        if count == 1:
            if ind == 1 or ind == n-1 or nums[ind-2] < nums[ind] or (ind<n-1 and nums[ind+1]>nums[ind-1]):
                return True
        return False
                