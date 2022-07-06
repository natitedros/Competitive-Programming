class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = len(nums)
        left = {}
        right = {}
        rtol = 0
        ltor = 0
        for i in range(l):
            if nums[i]%2 == 0:
                ltor += 1
            else:
                left[i] = ltor+1
                ltor = 0
            if nums[l-i-1]%2 == 0:
                rtol += 1
            else:
                right[l-i-1] = rtol+1
                rtol = 0
        nice = 0
        odd = 0
        lt = 0
        while lt < l and nums[lt]%2 == 0:
            lt += 1
        rt = lt
        odd += 1
        while rt+1 < l and odd != k:
            rt += 1
            if nums[rt]%2:
                odd += 1
        while rt < l and nums[rt]%2:
            nice += left[lt]*right[rt]
            lt += 1
            while lt < l and nums[lt]%2 == 0:
                lt += 1
            rt += 1
            while rt < l and nums[rt]%2 == 0:
                rt += 1
        return nice