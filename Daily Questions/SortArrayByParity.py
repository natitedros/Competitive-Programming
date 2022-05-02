class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = 0
        even = 0
        l = len(nums)
        while even < l:
            while odd < l and nums[odd]%2 == 0:
                odd += 1
            even = odd + 1
            while even < l and nums[even]%2 != 0:
                even += 1
            if even < l:
                nums[odd], nums[even] = nums[even], nums[odd]
        return nums