class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        lst = []
        for i in freq:
            temp = [freq[i], i]
            lst.append(temp)
        lst.sort(reverse = True)
        size = len(arr)
        res = 0
        decr = 0
        i = 0
        while decr < size/2:
            decr += lst[i][0]
            res += 1
            i += 1
        return res