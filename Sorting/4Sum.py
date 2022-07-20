class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []
        visited = set()
        for i in range(l):
            for j in range(i+1,l):
                left = j+1
                right = l-1
                while left < right:
                    temp = nums[i]+nums[j]+nums[left]+nums[right]
                    if temp < target:
                        left += 1
                    elif temp > target:
                        right -= 1
                    else:
                        ans = [nums[i],nums[j],nums[left],nums[right]]
                        ans.sort()
                        tup = tuple(ans)
                        if tup not in visited:
                            res.append(ans)
                            visited.add(tup)
                        left += 1
        return res