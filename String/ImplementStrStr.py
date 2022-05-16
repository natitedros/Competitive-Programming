class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hayLen = len(haystack)
        needleLen = len(needle)
        if needleLen == 0:
            return 0
        elif needleLen > hayLen:
            return -1
        left = 0
        right = needleLen
        while right <= hayLen:
            if haystack[left:right] == needle:
                return left
            else:
                left += 1
                right += 1
        return -1