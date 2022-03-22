class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        left = 0
        right = len(nums)-1
        while right > left:
            if nums[left] + nums[right] > k:
                right -=1
            elif nums[left] + nums[right] < k:
                left +=1
            elif nums[left] + nums[right] == k:
                left +=1
                right -=1
                res +=1
        return res