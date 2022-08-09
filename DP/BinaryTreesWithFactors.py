class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp = {}
        mod = ((10**9)+7)
        for i in range(len(arr)):
            tree = 0
            for key in dp.keys():
                if arr[i]/key in dp:
                    tree += (dp[arr[i]/key]*dp[key])%mod
            dp[arr[i]] = 1+tree
        return sum(dp.values())%mod