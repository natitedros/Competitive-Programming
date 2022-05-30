class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = 1
        b = 1
        if dividend < 0:
            a = -1
        if divisor < 0:
            b = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        for i in range(31,-1,-1):
            temp = divisor<<i
            if temp <= dividend:
                dividend -= temp
                res += 1<<i
        res = res*a*b
        res = min(res,(2**31)-1)
        res = max(res, -2**31)
        return res