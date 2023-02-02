class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        acc = set()
        for num in nums:
            if num: acc.add(num)
        return len(acc)
        