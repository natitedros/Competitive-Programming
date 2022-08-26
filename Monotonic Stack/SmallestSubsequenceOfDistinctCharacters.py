class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        stk = []
        distinct = set()
        for char in s:
            if char not in distinct:
                while stk and stk[-1] > char and freq[stk[-1]] > 1:
                    temp = stk.pop()
                    freq[temp] -= 1
                    distinct.remove(temp)
                stk.append(char)
                distinct.add(char)
            else:
                freq[char] -= 1
        return ''.join(stk)