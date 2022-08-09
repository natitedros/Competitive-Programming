class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        l = len(s)
        dp = defaultdict(int)
        for i in range(l-1,-1,-1):
            maxLen = 0
            for j in range(-1*k,k+1):
                if 97<= ord(s[i])+j <= 122:
                    maxLen = max(maxLen,dp[chr(ord(s[i])+j)])
            dp[s[i]] = 1+maxLen
        return max(dp.values())