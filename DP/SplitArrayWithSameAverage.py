class Solution:
    def isPossible(self, nums):
        sm = sum(nums)
        for i in range(1, len(nums)):
            if (i*sm)%len(nums) == 0:
                return True
        return False
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # Pruning
        if not self.isPossible(nums):
            return False

        # Build a set for all the possible combination sums of the smaller set
        dp = defaultdict(set)
        dp[0].add(0)
        for num in nums:
            for i in range(len(nums)//2, 0, -1):
                for val in dp[i-1]:
                    dp[i].add(num+val)
        sm = sum(nums)

        # Use math to validate possibility. If the Smalller set sum equals 
        # the ratio of the total sum * (smallerSize/totalSize), the array can be split.
        for i in range(1, len(nums)//2 + 1):
            for val in dp[i]:
                if (i*sm) / len(nums) == val:
                    return True
        return False

