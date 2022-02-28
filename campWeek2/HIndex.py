class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n-1
        res = []
        while left <= right:
            mid = left + (right-left)//2
            if n-mid <= citations[mid]:
                right = mid-1
                res.append(n-mid)
            else:
                left = mid+1
        if res:
            return max(res)
        return 0