class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        arr, d, count = [], {}, 0
        for i in range(n):
            if s[i] == "|":
                arr.append(i)
                d[i] = count
            else:
                count += 1
        
        def lower(q):
            left,right = 0, len(arr)-1
            while left <= right:
                mid = left + (right-left)//2
                if arr[mid] < q:
                    left = mid+1
                else:
                    right = mid-1
            return left
                    
        def upper(q):
            left,right = 0, len(arr)-1
            while left <= right:
                mid = left + (right-left)//2
                if arr[mid] > q:
                    right = mid-1
                else:
                    left = mid+1
            return right
        
        res = []
        for left,right in queries:
            l=lower(left)
            r=upper(right)
            if l < r:
                res.append(d[arr[r]]-d[arr[l]])
            else:
                res.append(0)
        return res
