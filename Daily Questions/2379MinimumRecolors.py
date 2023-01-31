class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minWhite = inf
        count = 0
        left = 0
        for right in range(len(blocks)):
            if blocks[right] == "W":
                count += 1
            if right-left+1 == k:
                minWhite = min(minWhite, count)
                if blocks[left] == "W":
                    count -= 1
                left += 1
        return minWhite