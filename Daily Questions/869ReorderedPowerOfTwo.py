class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        temp = n
        freq = defaultdict(int)
        length = 0
        while temp:
            freq[temp%10] += 1
            temp //= 10
            length += 1
        power = 0
        pLen = 0
        while pLen <= length:
            d = defaultdict(int)
            p = 2**power
            pLen = 0
            while p:
                d[p%10] += 1
                p //= 10
                pLen += 1
            if d == freq:
                return True
            power += 1
        return False