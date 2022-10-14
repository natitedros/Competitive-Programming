class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append((prefix[-1]+(num%k))%k)
        res = 0
        freq = defaultdict(int)
        for i in range(n+1):
            if freq[prefix[i]]:
                res += freq[prefix[i]]
            freq[prefix[i]] += 1
        return res
                    