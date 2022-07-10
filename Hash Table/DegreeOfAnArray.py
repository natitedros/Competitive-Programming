class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        maxFreq = 0
        minLen = 0
        d = {}
        for i in range(l):
            if nums[i] not in d:
                d[nums[i]] = [i,0]
            d[nums[i]][1] += 1
            if d[nums[i]][1] > maxFreq:
                maxFreq = d[nums[i]][1]
                minLen = i - d[nums[i]][0] + 1
            elif d[nums[i]][1] == maxFreq:
                minLen = min(minLen, i - d[nums[i]][0] + 1)
        return minLen