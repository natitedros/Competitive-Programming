class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        sArr = []
        tArr = []
        for i in range(sLen):
            if sArr and s[i] == '#':
                sArr.pop()
            elif s[i] != '#':
                sArr.append(s[i])
        for i in range(tLen):
            if tArr and t[i] == '#':
                tArr.pop()
            elif t[i] != '#':
                tArr.append(t[i])
        return sArr==tArr