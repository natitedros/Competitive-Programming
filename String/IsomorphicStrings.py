class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        used = set()
        sLen = len(s)
        for i in range(sLen):
            if s[i] not in d:
                if t[i] in used:
                    return False
                d[s[i]] = t[i]
                used.add(t[i])
            else:
                if not d[s[i]] == t[i]:
                    return False
        return True