class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        freq = defaultdict(int)
        res = 0
        for p in prefix:
            if freq[p-k]:
                res += freq[p-k]
            freq[p] += 1
        return res