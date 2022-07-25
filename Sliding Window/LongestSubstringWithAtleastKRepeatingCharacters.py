class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def rec(left,right):
            if right-left+1 < k:
                return 0
            freq = defaultdict(int)
            for i in range(left,right+1):
                freq[s[i]] += 1
            stop,ptr = left,left
            maxLen = 0
            while ptr < right+1:
                if freq[s[ptr]] < k:
                    maxLen = max(maxLen,rec(stop,ptr-1))
                    stop = ptr+1
                ptr += 1
            if stop == left:
                maxLen = right-left+1
            else:
                maxLen = max(maxLen,rec(stop,right))
            return maxLen
        n = len(s)
        if k == 1:
            return n
        return rec(0,n-1)