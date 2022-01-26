class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return "0"
        else:
            prevSize = (2**(n-1))/2
            if k > prevSize:
                res = self.kthGrammar(n-1, k-prevSize)
                if res == "0":
                    return "1"
                else:
                    return "0"
            else:
                return self.kthGrammar(n-1, k)