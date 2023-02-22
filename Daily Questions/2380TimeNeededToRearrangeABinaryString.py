class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count = 0
        while "01" in s:
            s = s.replace("01", "10")
            count += 1
        return count