class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = 1
        stat = None
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1] and stat != False:
                stat = False
                length += 1
            elif nums[i] > nums[i-1] and stat != True:
                stat = True
                length += 1
        return length