class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        prevZero,one = 0,0
        res1 = 0
        ans=0
        for i in range(n-1,-1,-1):
            if s[i] == "0":
                res1 += one*prevZero
                ans+=res1
                one = 0
                prevZero += 1
            else:
                one += 1
        res2 = 0
        prevOne,zero = 0,0
        for i in range(n-1,-1,-1):
            if s[i] == "1":
                res2 += zero*prevOne
                ans+=res2
                zero = 0
                prevOne += 1
            else:
                zero += 1
        return ans
                