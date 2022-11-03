class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        firstLeft = 0
        firstRight = firstLen
        maxVal = 0
        while firstRight < len(prefix):
            secondLeft = 0
            secondRight = secondLen
            while secondRight < len(prefix):
                if secondRight <= firstLeft or secondLeft >= firstRight:
                    summation = prefix[firstRight]-prefix[firstLeft]+prefix[secondRight]-prefix[secondLeft]
                    maxVal = max(maxVal, summation)
                secondLeft += 1
                secondRight += 1
            firstLeft += 1
            firstRight += 1
        return maxVal
            