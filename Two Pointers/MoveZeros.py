class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        placer = 0
        for i in range(l):
            if nums[i]:
                nums[i], nums[placer] = nums[placer], nums[i]
                placer += 1