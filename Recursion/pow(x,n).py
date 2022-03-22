class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n<0:
            x=1/x
            n=abs(n)
        elif n==0:
            return 1
        temp = n%2
        return (self.myPow(x,n//2)**2)*(x**(temp))