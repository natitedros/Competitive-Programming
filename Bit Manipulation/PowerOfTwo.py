class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        length = n.bit_length()
        return 1<<(length-1) == n