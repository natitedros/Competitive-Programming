class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        if n==0:
            return ""
        setstr = set(s)
        found = False
        res=""
        for i in range(n):
            if s[i].swapcase() not in setstr:
                found = True
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                if len(s2)>len(s1):
                    res = s2
                else:
                    res = s1
                break
        if not found:
            return s
        return res