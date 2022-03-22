class Solution:
    dicts = {}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        if n in self.dicts:
            return self.dicts[n]
        self.dicts[n] = self.fib(n-1)+self.fib(n-2)
        return self.dicts[n]