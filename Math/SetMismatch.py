class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        setSum = sum(set(nums))
        trueSum = 0
        for i in range(1, len(nums)+1):
            trueSum += i
        return [sum(nums)-setSum, trueSum-setSum]