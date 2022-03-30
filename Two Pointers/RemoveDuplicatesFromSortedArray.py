class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 1
        back = 0
        front = 1
        reps = 0
        while front < l:
            while front < l and nums[front] == nums[back]:
                nums[front] = 101
                front += 1
                reps += 1
            back = front
            front += 1
        nums.sort()
        return l-reps