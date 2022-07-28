class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in range(len(nums)):
            if not count:
                res = nums[i]
                count += 1
            elif nums[i] != res:
                count -= 1
            else:
                count += 1
        return res