class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = len(nums)
        chance = k
        maxLength = 0
        left = 0
        right = 0
        while right < l:
            if left == right:
                chance = k
            if not chance and nums[right] == 0:
                if right-left > maxLength:
                    maxLength = right-left
                if nums[left] == 0:
                    chance += 1
                left += 1
            elif nums[right] == 0:
                chance -= 1
                right += 1
            else:
                right += 1
        if right-left > maxLength:
            maxLength = right-left
        return maxLength 