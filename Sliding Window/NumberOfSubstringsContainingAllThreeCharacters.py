class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        left, right = 0,0
        window = Counter()
        res = 0
        for right in range(n):
            window[s[right]] += 1
            while left < right and window["a"] and window["b"] and window["c"]:
                res += n-right
                window[s[left]] -= 1
                left += 1
        return res