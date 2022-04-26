class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k%l
        nums[:l-k] = reversed(nums[:l-k])
        nums[l-k:] = reversed(nums[l-k:])
        nums.reverse()