class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        res = []
        for i in range(2**l):
            length = i.bit_length()
            temp = []
            for j in range(length):
                if i&(1<<j):
                    temp.append(nums[l-j-1])
            res.append(temp)
        return res