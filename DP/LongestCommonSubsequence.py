# Top Down
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = {}
        def rec(ptr1,ptr2):
            if (ptr1,ptr2) in dp:
                return dp[(ptr1,ptr2)]
            if ptr1>=len1 or ptr2>=len2:
                return 0
            if text1[ptr1] == text2[ptr2]:
                dp[(ptr1,ptr2)] = 1+rec(ptr1+1,ptr2+1)
            else:
                dp[(ptr1,ptr2)] = max(rec(ptr1+1,ptr2),rec(ptr1,ptr2+1))
            return dp[(ptr1,ptr2)]
        return rec(0,0)
# Botmo Up
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        dp = defaultdict(int)
        for i in range(len1-1,-1,-1):
            for j in range(len2-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[(i,j)] = 1+dp[(i+1,j+1)]
                else:
                    dp[(i,j)] = max(dp[(i+1,j)],dp[(i,j+1)])
        return dp[(0,0)]
        