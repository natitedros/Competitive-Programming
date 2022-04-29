class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        l = len(s)
        letters = set()
        maxLetter = 0
        while right < l:
            while s[right] in letters and left<= right:
                letters.remove(s[left])
                left += 1
            if left>right:
                right = left
            letters.add(s[right])
            length = len(letters)
            if length > maxLetter:
                maxLetter = length
            right += 1
        return maxLetter