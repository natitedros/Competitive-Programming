arr = [4,3,9,7,2]

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

    if (small  != i):
        arr[small] , arr[i] = arr[i] ,arr[small]
        downheap(arr,n,small)
        
       

def buildHeap(arr,n):

    for i in range(n):
        heapify(arr, n,i )
 
def HeapSort(arr, n):
    res = []
    buildHeap(arr,len(arr))
    while(arr):
        res.append(arr.pop(0))
        heapify(arr,len(arr),0)
        print(res,arr)
        
    print(res)
    

HeapSort(arr, len(arr))

print(arr)
