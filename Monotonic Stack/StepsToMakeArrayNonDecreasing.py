class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stk = []
        for i in range(len(nums)-1,-1,-1):
            count = 0
            while stk and stk[-1][0] < nums[i]:
                count = max(count+1,stk[-1][1])
                stk.pop()
            stk.append([nums[i],count])
        res = 0
        for val in stk:
            res = max(val[1],res)
        return res