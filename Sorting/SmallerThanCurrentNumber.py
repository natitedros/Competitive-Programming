class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j!=i and nums[j]<nums[i]:
                    arr[i]+=1
        return arr