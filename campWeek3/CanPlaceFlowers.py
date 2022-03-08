class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        possible = 0
        current = 0
        prev = current-1
        nxt = current+1
        length = len(flowerbed)
        while current<length:
            if (prev<0 or flowerbed[prev] == 0) and (nxt>=length or flowerbed[nxt] == 0):
                if flowerbed[current] == 0:
                    flowerbed[current] = 1
                    possible += 1
            current += 1
            prev += 1
            nxt += 1
        if possible >= n:
            return True
        return False