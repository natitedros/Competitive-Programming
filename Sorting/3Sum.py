class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        added = set()
        res = []
        for i in range(l-2):
            left = i+1
            right = l-1
            while left < right:
                if nums[left] + nums[right] + nums[i] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    if (nums[left],nums[right],nums[i]) not in added:
                        added.add((nums[left],nums[right],nums[i]))
                        added.add((nums[left],nums[i],nums[right]))
                        added.add((nums[right],nums[left],nums[i]))
                        added.add((nums[right],nums[i],nums[left]))
                        added.add((nums[i],nums[left],nums[right]))
                        added.add((nums[i],nums[right],nums[left]))
                        res.append([nums[left],nums[right],nums[i]])
                    left += 1
                    right -= 1
        return res