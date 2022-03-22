class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                temp = stack.pop()
                s = s[0:temp:1] + s[i:temp:-1] + s[i:len(s):1]
        for i in s:
            if i != ")" and i != "(":
                res.append(i)
        res = "".join(res)
        return res