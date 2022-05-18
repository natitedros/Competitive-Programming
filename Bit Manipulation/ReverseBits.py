class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for i in range(32):
            rev = rev<<1
            if n & (1<<i):
                rev += 1
        return rev