class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        p1, p2 = 0, 0
        while True:
            if p1 == len(nums1) and p2 == len(nums2):
                break
            elif p1 < len(nums1) and p2 < len(nums2):
                if nums1[p1] < nums2[p2]:
                    nums.append(nums1[p1])
                    p1 += 1
                else:
                    nums.append(nums2[p2])
                    p2 += 1
            elif p1 < len(nums1):
                nums.append(nums1[p1])
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1
        if len(nums)%2 == 0:
            return (nums[len(nums)//2] + nums[(len(nums)//2) - 1]) / 2
        return nums[len(nums)//2]