class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        half = n//2
        pal = palindrome[0:half]
        if pal == "a"*(half):
            return palindrome[0:n-1]+"b"
        i = 0
        while pal[i] == "a":
            i+=1
        res = pal[0:i]+"a"+palindrome[i+1:n]
        return res