class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        temp = (10**9)+7
        freq = defaultdict(int)
        for d in deliciousness:
            freq[d] += 1
        res = 0
        for d in deliciousness:
            freq[d] -= 1
            for i in range(22):
                power = 1<<i
                res += freq[power-d]
        return res%temp