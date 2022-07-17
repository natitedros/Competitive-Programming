class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        l = len(nums)
        left = 0
        right = l
        while left<right:
            if nums[left] == val:
                right -= 1
                nums[left], nums[right] = nums[right], nums[left]
            else:
                k += 1
                left += 1
        return k