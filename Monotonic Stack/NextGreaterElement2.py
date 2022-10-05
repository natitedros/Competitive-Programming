class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        d = {}
        stk = []
        for i,num in enumerate(nums):
            while stk and nums[stk[-1]] < num:
                d[stk.pop()] = i
            stk.append(i)
        for i,num in enumerate(nums):
            while stk and nums[stk[-1]] < num:
                temp = stk.pop()
                if stk[-1] not in d:
                    d[temp] = i
            stk.append(i)
        res = []
        for i in range(len(nums)):
            if i not in d:
                res.append(-1)
            else:
                res.append(nums[d[i]])
        return res