class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        sm = ((l+1)*l)//2
        for num in nums:
            sm -= num
        return sm