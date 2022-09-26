class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqt = [0]*58
        for char in t:
            freqt[ord(char)-65] += 1
        res = [-inf,inf]
        left,right = 0,0
        window = [0]*58
        while right < len(s):
            window[ord(s[right])-65] += 1
            isSubset = True
            for i in range(58):
                if window[i] < freqt[i]:
                    isSubset = False
                    break
            while left <= right and isSubset:
                if right-left+1 < res[1]-res[0]+1:
                    res[0],res[1] = left,right
                window[ord(s[left])-65] -= 1
                if window[ord(s[left])-65] < freqt[ord(s[left])-65]:
                    isSubset = False
                left += 1
            right += 1
        if res == [-inf,inf]:
            return ""
        return s[res[0]:res[1]+1]
                        