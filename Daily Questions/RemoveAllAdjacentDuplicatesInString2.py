class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for char in s:
            if not stk:
                stk.append([char,1])
            else:
                if stk[-1][0] == char:
                    stk[-1][1] += 1
                    if stk[-1][1] == k:
                        stk.pop()
                else:
                    stk.append([char,1])
        res = []
        for char in stk:
            res.append(char[0]*char[1])
        return ''.join(res)