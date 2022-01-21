class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.bits(n)[k-1]
    def bits(self,n):
        bts = ""
        if n == 1:
            return "0"
        else:
            bts = self.bits(n-1)
            res = bts + "1" + self.reverse(self.invert(bts))
            return res
    def reverse(self,x):
        return x[::-1]
    def invert(self,x):
        ls = []
        for i in x:
            if i == "1":
                ls.append("0")
            else:
                ls.append("1")
        return ''.join(ls)