class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber :
            columnNumber -= 1
            rem = columnNumber % 26
            res.append(chr(65+rem))
            columnNumber //= 26
        res.reverse()
        return ''.join(res)