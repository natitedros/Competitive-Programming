class Solution:
    def findHash(self, left, right, prev, haystack):
        prev -= (ord(haystack[left]) - ord("a") + 1)
        prev /= 3
        prev += (ord(haystack[right]) - ord("a") + 1)*(3**(right-left-1))
        return prev
    
    def strStr(self, haystack: str, needle: str) -> int:
        needle_hash = 0
        haystk_hash = 0
        if len(haystack) < len(needle):
            return -1
        for i, char in enumerate(needle):
            needle_hash += (3**i)*(ord(char) - ord("a") + 1)
            haystk_hash += (3**i)*(ord(haystack[i]) - ord("a") + 1)
        if haystk_hash == needle_hash:
            if haystack[:len(needle)] == needle:
                return 0
        left, right = 0, len(needle)
        while right < len(haystack):
            haystk_hash = self.findHash(left, right, haystk_hash, haystack)
            left += 1
            right += 1
            if haystk_hash == needle_hash:
                if haystack[left:right] == needle:
                    return left
        return -1
        