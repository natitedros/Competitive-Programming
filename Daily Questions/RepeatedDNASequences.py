class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        right = 9
        l = len(s)
        d = {}
        window = ""
        while right < l:
            if window == "":
                window = s[:right+1]
            else:
                window = window[1:] + s[right]
            if window not in d:
                d[window] = 0 
            d[window] += 1
            right += 1
        res = []
        if d:
            for key in d.keys():
                if d[key] > 1:
                    res.append(key)
        return res