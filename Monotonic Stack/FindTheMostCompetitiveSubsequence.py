class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        remove = n-k
        stk = []
        for i in range(n):
            while stk and stk[-1] > nums[i] and remove > 0:
                remove -= 1
                stk.pop()
            stk.append(nums[i])
        while remove > 0:
            remove -= 1
            stk.pop()
        return stk