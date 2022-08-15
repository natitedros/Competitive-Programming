class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res = 0
        for i in range(len(s)):
            if not i or d[s[i]] <= d[s[i-1]]:
                res += d[s[i]]
            elif d[s[i]] > d[s[i-1]]:
                res += d[s[i]]-(2*d[s[i-1]])
        return res