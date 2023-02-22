class Solution:
    def calculate(self, s: str) -> int:
        sums, sign, i = 0, 1, 0
        stack = []
        while i < len(s):
            char = s[i]
            if char.isdigit():
                val = 0
                # Multiple Digit
                while i < len(s) and s[i].isdigit():
                    val = val*10 + int(s[i])
                    i+=1
                i-=1
                sums+=val*sign
                sign = 1
            elif char == '(':
                stack.append(sums)
                stack.append(sign)
                sums,sign = 0,1
            elif char == ')':
                sums*=stack.pop()
                sums+=stack.pop()
            elif char =='-':
                sign*=-1
            i+=1

        return sums
