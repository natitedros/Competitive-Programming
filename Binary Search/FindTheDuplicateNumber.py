class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        front = 1
        back = 0
        n = len(nums)
        if n == 1:
            return -1
        while front < n:
            if nums[front] == nums[back]:
                break
            front += 1
            back += 1
        return nums[front]