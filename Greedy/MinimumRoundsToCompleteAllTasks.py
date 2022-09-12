class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = defaultdict(int)
        res = 0
        for task in tasks:
            freq[task] += 1
        for key in freq.keys():
            if freq[key] == 1:
                return -1
            res += ceil(freq[key]/3)
        return res