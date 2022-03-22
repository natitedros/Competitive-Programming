class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairArr = []
        for i in range(len(nums)//2):
            pairArr.append(nums[i] + nums[-1-i])
        return max(pairArr)