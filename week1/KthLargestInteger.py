class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        nums.sort()
        nums.reverse()
        return str(nums[k-1])