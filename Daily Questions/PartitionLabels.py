class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l = len(s)
        d = defaultdict(list)
        for i in range(l):
            d[s[i]].append(i)
        prevPtr = -1
        lastIndex = 0
        res = []
        lastIndex = d[s[0]][-1]
        for key in d.keys():
            if lastIndex>d[key][0]:
                lastIndex = max(d[key][-1], lastIndex)
            elif lastIndex==d[key][0]:
                continue
            else:
                res.append(lastIndex-prevPtr)
                prevPtr = lastIndex
                lastIndex = d[key][-1]
        res.append(lastIndex-prevPtr)
        return res 