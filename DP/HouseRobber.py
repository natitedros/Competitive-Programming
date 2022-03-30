class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        d = {}
        def house(ind):
            nonlocal l
            if ind>=l:
                return 0
            if ind not in d:
                maxVal = 0
                for i in range(ind+2,l):
                    temp = house(i)
                    if temp > maxVal:
                        maxVal = temp
                d[ind] = nums[ind] + maxVal   
            return d[ind]
        maxVal = 0
        for i in range(l):
            temp = house(i)
            if temp > maxVal:
                maxVal = temp
        return maxVal