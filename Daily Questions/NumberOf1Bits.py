class Solution:
    def hammingWeight(self, n: int) -> int:
        length = n.bit_length()
        count = 0
        for i in range(length):
            if n & (1<<i):
                count += 1
        return count