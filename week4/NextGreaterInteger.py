class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dicts = {}
        for i in range(len(nums2)):
            dicts[nums2[i]] = -1
            if stack == []:
                stack.append(nums2[i])
            else:
                if nums2[i] < stack[-1]:
                    stack.append(nums2[i])
                else:
                    while len(stack) > 0 and nums2[i]>stack[-1]:
                        dicts[stack.pop()] = nums2[i]
                    stack.append(nums2[i])
        res = []
        for i in range(len(nums1)):
            res.append(dicts[nums1[i]])
        return res