class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = defaultdict(int)
        res = 0
        for r in answers:
            if freq[r] == 0:
                res += r+1
            freq[r] += 1
            if freq[r] == r+1:
                freq[r] = 0
        return res