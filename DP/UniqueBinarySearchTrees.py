class Solution:
    def numTrees(self, n: int) -> int:
        dp = defaultdict(int)
        dp[0], dp[1] = 1, 1
        dp[2] = 2
        for i in range(3,n+1):
            temp = 0
            for j in range(1,i+1):
                temp += dp[j-1]*dp[i-j]
            dp[i] = temp
        return dp[n]
