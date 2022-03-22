arr = [4, 1, 3, 9, 7,8,2,5]

def heapify(arr, n, i):
   upheap(arr,n,i)
   downheap(arr,n,i)

def upheap(arr,n,i):
    p = (i-1) //2
    while p >= 0 and p < n and arr[i] < arr[p]: 
        arr[p] , arr[i] = arr[i] , arr[p]
        i = p
        p = (i-1) //2

def downheap(arr,n,i):
    l = 2 * i + 1
    r = 2 * i + 2
    small = i

    if l < n and arr[l] < arr[small]:
        small = l
    
    if r < n and arr[r] < arr[small]:
        small = r

    if (small != i):
        arr[small] , arr[i] = arr[i] ,arr[small]
        downheap(arr,n,small)
        
       

def buildHeap(arr,n):

    for i in range(n):
        heapify(arr, n, n-i-1)
 
def HeapSort(arr, n):
    res = []
    buildHeap(arr,n)
    while(arr):
        res.append(arr.pop(0))
        heapify(arr,len(arr),0)
        
        
    print(res)
    

HeapSort(arr, len(arr))


class Solution:
    # Heapify function to maintain heap property.
    def heapify(self, arr, n, i):
        # code here
        self.downheap(arr, n, i)
        # self.upheap(arr, n, i-1)

    def upheap(self, arr, n, i):
        p = i // 2
        while p > 0 and p < n and arr[i] < arr[p]:
            arr[p], arr[i] = arr[i], arr[p]
            i = p
            p = i // 2

    def downheap(self, arr, n, i):
        l = 2 * i + 1
        r = 2 * i + 2
        small = i
        if l < n and arr[l] < arr[small]:
            small = l
        if r < n and arr[r] < arr[small]:
            small = r
        if (small != i):
            arr[small], arr[i] = arr[i], arr[small]
            self.downheap(arr, n, small)

    # Function to build a Heap from array.
    def buildHeap(self, arr, n):
        # code here
        i = n//2 - 1
        for i in range(i, -1, -1):
            self.heapify(arr, n, i)

    # Function to sort an array using Heap Sort.

    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for j in range(n-1, -1, -1):
            arr[0], arr[j] = arr[j], arr[0]
            self.heapify(arr, j, 0)


