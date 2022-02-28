class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        mid = 0
        arr = []
        while left <= right:
            mid = left + (right-left)//2
            tot = 0
            for number in nums:
                tot += math.ceil(number/mid)
            if tot <= threshold:
                arr.append(mid)
                right = mid-1
            elif tot > threshold:
                left = mid+1
        return min(arr)