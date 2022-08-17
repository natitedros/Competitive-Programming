class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        n = len(num)
        for i in range(n):
            while stk and stk[-1]>num[i] and k:
                k -= 1
                stk.pop()
            if stk or num[i] != "0":
                stk.append(num[i])
        res = ""
        for i in range(len(stk)-k):
            res += stk[i]
        if res == "": return "0"
        return res