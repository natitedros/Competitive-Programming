class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//2
        left, right = nums[:n], nums[n:]
        leftSum, rightSum = sum(left), sum(right)
        res = inf
        for i in range(n+1): 
            # sorting in advance and search the right numbers for the left numbers
            vals = sorted(2*sum(combo)-leftSum for combo in combinations(left, i))
            for combo in combinations(right, n-i): 
                differenece = 2*sum(combo) - rightSum
                k = bisect_left(vals, -differenece)
                if k: 
                    res = min(res, abs(vals[k-1] + difference))
                if k < len(vals): 
                    res = min(res, abs(vals[k] + difference))
        return res 