class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total = 0
        for num in nums:
            total ^= num
        total = total & -total
        first, second = 0, 0
        for num in nums:
            if num & total:
                first ^= num
            else:
                second ^= num
        return [first, second]
        