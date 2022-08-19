class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hours(k):
            hour = 0
            for pile in piles:
                hour += pile//k
                if pile%k:
                    hour += 1
            return hour
        
        left, right = 1, max(piles)
        while left <= right:
            k = left + (right-left)//2
            if hours(k) > h:
                left = k+1
            else:
                right = k-1
                
        return left