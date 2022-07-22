class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right,maxNum,res = 0,0,0,0
        while right < len(nums):
            k -= (right-left)*(nums[right]-maxNum)
            while k < 0:
                k += nums[right]-nums[left]
                left+=1
            maxNum = max(maxNum,nums[right])
            res = max(res,right-left+1)
            right += 1
        return res