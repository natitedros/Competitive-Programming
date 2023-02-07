class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using quick select the time complexity is o(Nlog(N)) 
        # but the base fo the logarithm is optimized
        # which makes the time complexity converge to Linear Time geometrically!
        pivot = choice(nums)
        greater = [x for x in nums if x > pivot]
        equal = [x for x in nums if x == pivot]
        less = [x for x in nums if x < pivot]
        if k <= len(greater):
            return self.findKthLargest(greater, k)
        elif k > len(greater) + len(equal):
            return self.findKthLargest(less, k - len(greater) - len(equal))
        else:
            return equal[0]