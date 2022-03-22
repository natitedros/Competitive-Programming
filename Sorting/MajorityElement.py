class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = len(nums)/3
        res = set()
        nums.sort()
        count = 1
        for i in range(len(nums)):
            if i != 0 and nums[i-1] != nums[i]:
                count = 1
            if i == 0 and count > freq:
                res.add(nums[i])
            elif nums[i-1] == nums[i]:
                count += 1
            if count > freq:
                res.add(nums[i])
                count = 1
        return res