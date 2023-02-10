class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0,0
        minVal = inf
        for i in range(len(nums)):
            nums[i] = nums[i]**2
            if nums[i] < minVal:
                minVal = nums[i]
                left = right = i
        res = []
        while left >= 0 and right < len(nums):
            if left == right:
                res.append(nums[left])
                left -= 1
                right += 1
            elif nums[left] < nums[right]:
                res.append(nums[left])
                left -= 1
            else:
                res.append(nums[right])
                right += 1
        while left >= 0:
            res.append(nums[left])
            left -= 1
        while right < len(nums):
            res.append(nums[right])
            right += 1
        return res