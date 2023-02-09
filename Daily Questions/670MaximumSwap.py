class Solution:
    def maximumSwap(self, num: int) -> int:
        numbers = list(str(num))
        res = num
        for i in range(len(numbers)):
            for j in range(i, len(numbers)):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                res = max(res, int("".join(numbers)))
                numbers[i], numbers[j] = numbers[j], numbers[i]
        return res