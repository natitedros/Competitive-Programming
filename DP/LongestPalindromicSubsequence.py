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