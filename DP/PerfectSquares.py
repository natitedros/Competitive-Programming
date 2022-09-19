class Solution:
    def numSquares(self, n: int) -> int:
        perfect = []
        num = 1
        while num**2<=n:
            perfect.append(num**2)
            num += 1
        dp = [inf]*(n+1)
        dp[0], dp[1] = 0, 1
        for i in range(2,n+1):
            for p in perfect:
                if i-p < 0:
                    break
                if 1+dp[i-p] < dp[i]:
                    dp[i] = 1+dp[i-p]
        return dp[n]