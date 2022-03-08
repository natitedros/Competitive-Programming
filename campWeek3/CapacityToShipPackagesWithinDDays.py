class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        minVal = max(weights)
        maxVal = sum(weights)
        ans = maxVal
        while minVal <= maxVal:
            mid = minVal + (maxVal-minVal)//2
            sm = 0
            count = 0
            for i in range(n):
                if sm + weights[i] > mid:
                    sm = 0
                    count += 1
                sm += weights[i]
            count += 1
            if count > days:
                minVal = mid+1
            elif count < days:
                ans = min(ans, mid)
                maxVal = mid-1
            else:
                maxVal -= 1
                ans = min(ans, mid)
        return ans