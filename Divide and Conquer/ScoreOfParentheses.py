# Divide And Conquer
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def rec(left,right):
            ans, bal = 0, 0
            stop = left
            for i in range(left,right+1):
                if s[i] == "(": 
                    bal += 1
                else:
                    bal -= 1
                if not bal:
                    if stop+1 == i:
                        ans += 1
                    else:
                        ans += 2*rec(stop+1,i-1)
                    stop = i+1
            return ans
        return rec(0,len(s)-1)

# Elegant One I wrote

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        opened = False
        stk = 0
        for char in s:
            if char == "(":
                stk += 1
                opened = True
            elif opened:
                stk -= 1
                res += 2**stk
                opened = False
            else:
                stk -= 1
        return res