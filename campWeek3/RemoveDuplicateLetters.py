class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        freq = {}
        for i in range(n):
            if s[i] not in freq:
                freq[s[i]] = 0
            freq[s[i]] += 1
        stk = []
        for i in range(n):
            if not stk:
                stk.append(s[i])
            else:
                while stk and s[i] <= stk[-1] and freq[stk[-1]] > 1 and s[i] not in stk:
                    freq[stk.pop()] -= 1
                if s[i] not in stk:
                    stk.append(s[i])
                else:
                    freq[s[i]] -= 1
        return ''.join(stk)