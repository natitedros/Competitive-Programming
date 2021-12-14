class Solution: 
    def select(self, arr, i):
        # code here 
        minPos = i
        for j in range(i, len(arr)):
            if arr[j]<arr[i]:
                minPos = j
        return minPos
    def selectionSort(self, arr,n):
        #code here
        arr.sort()