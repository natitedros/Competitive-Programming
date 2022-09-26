class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0]*n
        num = 0
        for i in range(n):
            if s[n-i-1] == "1":
                if num + (2**i) <= k:
                    num += 2**i
                    dp[n-i-1] = 1
            else:
                dp[n-i-1] = 1
        count = 0
        for val in dp:
            if val:
                count += 1
        return count