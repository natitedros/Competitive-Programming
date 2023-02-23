class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        m = {}
        return self.dfs(expression, m)
        
    def dfs(self, inp, m):
        if inp in m:
            return m[inp]
        if inp.isdigit():
            m[inp] = int(inp)
            return [int(inp)]
        ret = []
        for i, c in enumerate(inp):
            if c in "+-*":
                l = self.diffWaysToCompute(inp[:i])
                r = self.diffWaysToCompute(inp[i+1:])
                ret.extend(eval(str(x)+c+str(y)) for x in l for y in r)
        m[inp] = ret
        return ret