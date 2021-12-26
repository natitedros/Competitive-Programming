class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        you = len(piles)-2
        bob = 0
        res = 0
        while bob<you:
            res += piles[you]
            you -= 2
            bob += 1
        return res