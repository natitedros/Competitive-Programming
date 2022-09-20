# Top Down
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = {}
        def rec(left,right):
            if (left,right) in dp:  return dp[(left,right)]
            if left == right:   return 1
            elif left > right:  return 0
            elif s[left] == s[right]:
                dp[(left,right)] = 2+rec(left+1,right-1)
                return dp[(left,right)]
            else:
                dp[(left,right)] = max(rec(left,right-1),rec(left+1,right))
                return dp[(left,right)]
        return rec(0,len(s)-1)
# Bottom Up
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = defaultdict(int)
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i == j:
                    dp[(i,j)] = 1
                elif s[i] == s[j]:
                    dp[(i,j)] = 2+dp[(i+1,j-1)]
                else:
                    dp[(i,j)] = max(dp[(i+1,j)],dp[(i,j-1)])
        return dp[(0,n-1)]