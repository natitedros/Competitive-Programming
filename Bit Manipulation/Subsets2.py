class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique = set()
        l = len(nums)
        for i in range(2**l):
            length = i.bit_length()
            temp2 = []
            for j in range(length):
                if i&(1<<j):
                    temp2.append(nums[l-j-1])
            temp = tuple(temp2)
            if temp not in unique:
                unique.add(temp)
        return unique