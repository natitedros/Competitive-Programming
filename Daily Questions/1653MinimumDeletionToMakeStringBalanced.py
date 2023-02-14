class Solution:
    def minimumDeletions(self, s: str) -> int:
        #prefixsum
        bLeft = []
        prev = 0
        for i in range(len(s)):
            bLeft.append(prev+(s[i]=="b"))
            prev = bLeft[-1]
        aRight = []
        prev = 0
        for i in range(len(s)-1, -1, -1):
            aRight.append(prev+(s[i]=="a"))
            prev = aRight[-1]
        aRight.reverse()
        minVal = inf
        for i in range(len(s)):
            minVal = min(minVal, aRight[i]+bLeft[i]-1)
        return minVal