# Using DP 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        dp = {}
        def incSubsequence(ind):
            if ind in dp:
                return dp[ind]
            maxLen = 0
            for i in range(ind+1,l):
                if nums[i] > nums[ind]:
                    maxLen = max(maxLen,incSubsequence(i))
            dp[ind] = 1+maxLen
            return dp[ind]
        mx = 0
        for i in range(l):
            mx = max(mx,incSubsequence(i))
        return mx


# Using Binary Search 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        sub = []
        for i in range(l):
            if not sub or nums[i] > sub[-1]:
                sub.append(nums[i])
            elif nums[i] <= sub[0]:
                sub[0] = nums[i]
            else:
                left = 0
                right = len(sub)-1
                mid = 0
                while left < right:
                    mid = left + (right-left)//2
                    if sub[mid] < nums[i]:
                        left = mid+1
                    else:
                        right = mid
                sub[right] = nums[i]
        return len(sub)