class Solution: 
    def select(self, arr, i):
        # code here 
        minPos = i
        for j in range(i, len(arr)):
            if arr[j]<arr[minPos]:
                minPos = j
        return minPos
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            minIndex = self.select(arr, i)
            arr[i], arr[minIndex] = arr[minIndex], arr[i]