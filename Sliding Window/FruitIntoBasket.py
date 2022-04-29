class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = len(fruits)
        left = 0
        right = 0
        maxFruit = 0
        window = {}
        size = 0
        while right < l:
            if len(window) == 2 and fruits[right] not in window:
                temp = l
                for key, value in window.items():
                    if temp not in window or value < window[temp]:
                        temp = key
                        left = value + 1
                del window[temp]
            window[fruits[right]] = right
            if right-left+1 > maxFruit:
                maxFruit = right-left+1
            right += 1
        return maxFruit