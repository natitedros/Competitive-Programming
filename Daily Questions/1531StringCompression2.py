class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dp(i, prev, prevCount, left):
            if left < 0:
                return inf
            if i == len(s):
                return 0
            
            delete = dp(i + 1, prev, prevCount, left - 1)
            if s[i] == prev:
                keep = dp(i + 1, prev, prevCount + 1, left)
                if prevCount == 1 or len(str(prevCount)) < len(str(prevCount + 1)):
                    keep += 1
            else:
                keep = dp(i + 1, s[i], 1, left) + 1
            return min(keep, delete)
            
        return dp(0, '', 0, k)
            