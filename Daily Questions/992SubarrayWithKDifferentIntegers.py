class Solution:
    def atmostKDistinct(self, nums, k):
        left = 0
        freq = defaultdict(int)
        res = 0
        for right in range(len(nums)):
            freq[nums[right]] += 1
            while len(freq) > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            res += right-left+1
        return res
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        one = self.atmostKDistinct(nums, k)
        two = self.atmostKDistinct(nums, k-1)
        return one-two
            
