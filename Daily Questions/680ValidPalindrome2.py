class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        def rec(left, right, diff):
            if diff > 1:
                return False
            if left >= right:
                return True
            if s[left] != s[right]:
                return rec(left+1, right, diff+1) or rec(left, right-1, diff+1)
            return rec(left+1, right-1, diff)
        return rec(0, len(s)-1, 0)       