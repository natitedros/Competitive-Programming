# Using Merge sort 

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr1,arr2):
            arr = []
            ptr1,ptr2 = 0,0
            len1, len2 = len(arr1), len(arr2)
            while ptr1 < len1 or ptr2 < len2:
                if ptr1<len1 and ptr2<len2:
                    if arr2[ptr2] < arr1[ptr1]:
                        arr.append(arr2[ptr2])
                        ptr2 += 1
                    else:
                        arr.append(arr1[ptr1])
                        ptr1 += 1
                elif ptr1<len1:
                    arr.append(arr1[ptr1])
                    ptr1 += 1
                else:
                    arr.append(arr2[ptr2])
                    ptr2 += 1
            return arr
        def divide(arr):
            if len(arr) == 1:
                return arr
            temp = math.ceil(len(arr)/2)
            return mergeSort(divide(arr[:temp]),divide(arr[temp:]))
        return divide(nums)