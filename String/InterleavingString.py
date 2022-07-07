class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1len = len(s1)
        s2len = len(s2)
        s3len = len(s3)
        if s3len != s1len+s2len:
            return False
        dp = {}
        def dfs(ptr1,ptr2,i):
            if (ptr1,ptr2,i) in dp:
                return dp[(ptr1,ptr2,i)]
            if i>=s3len:
                return True
            if ptr1<s1len and ptr2<s2len and s3[i] == s1[ptr1] and s3[i] == s2[ptr2]:
                dp[(ptr1,ptr2,i)] = dfs(ptr1+1, ptr2,i+1) or dfs(ptr1, ptr2+1,i+1)
            elif ptr1<s1len and s3[i] == s1[ptr1]:
                dp[(ptr1,ptr2,i)] = dfs(ptr1+1, ptr2,i+1)
            elif ptr2<s2len and s3[i] == s2[ptr2]:
                dp[(ptr1,ptr2,i)] = dfs(ptr1, ptr2+1,i+1)
            else:
                return False
            return dp[(ptr1, ptr2,i)]
        return dfs(0,0,0)