# Top Down
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i > n:
                return 0
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            temp = 0
            if s[i] == "1":
                temp += dfs(i+1) + dfs(i+2)
            else:
                if s[i] == "2" and i+1 < n and int(s[i+1]) < 7:
                    temp += dfs(i+2)
                temp += dfs(i+1)
            dp[i] = temp
            return temp
        return dfs(0)
# Bottom Up
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        second = 0
        first = 1
        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                second = first
                first = 0
            else:
                temp = first
                if s[i] == "1" or (s[i] == "2" and i+1 < n and int(s[i+1]) < 7):
                    temp += second
                second = first
                first = temp
        return first