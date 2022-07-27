class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lent = len(t)
        lens = len(s)
        if lens != lent:
            return False
        freq = defaultdict(int)
        for i in range(lens):
            freq[s[i]] += 1
            freq[t[i]] -= 1
        for val in freq.values():
            if val != 0:
                return False
        return True