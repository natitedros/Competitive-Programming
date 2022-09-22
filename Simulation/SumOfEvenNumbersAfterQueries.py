class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        evenSum = 0
        for num in nums:
            if not num%2:
                evenSum += num
        for q in queries:
            if not nums[q[1]]%2:
                evenSum -= nums[q[1]]
            nums[q[1]] += q[0]
            if not nums[q[1]]%2:
                evenSum += nums[q[1]]
            res.append(evenSum)
        return res