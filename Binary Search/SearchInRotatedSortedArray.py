class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left,right = 0,n-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                if nums[mid] >= nums[left] or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > target:
                if nums[mid] <= nums[right] or nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return mid
        return -1
                