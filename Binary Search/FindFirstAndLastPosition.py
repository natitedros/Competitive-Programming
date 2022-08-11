class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        found = False
        if target not in nums:
            return [-1,-1]
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                found = True
                left = right = mid
                break
        while found:
            if left>=0 and nums[left] == target:
                left -= 1
            if right<len(nums) and nums[right] == target:
                right +=1
            if (left<0 or nums[left] != target) and (right >=len(nums) or nums[right] != target):
                found = False
                return [left+1,right-1]
#Improved
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        found = False
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                found = True
                left = right = mid
                break
        if not found:
            return [-1,-1]
        res = [-1,-1]
        while left>=0 and nums[left]==target:
            left -= 1
        res[0] = left+1
        while right<len(nums) and nums[right]==target:
            right += 1
        res[1] = right-1
        return res