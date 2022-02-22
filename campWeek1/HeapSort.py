arr = [4,3,9,7,2]

def heapify(arr, n, i):
    # Up Heap
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
    # print(l,r)
    small = i

    # if arr[l] < arr[small] and arr[r] < arr[small]:


    if l < n and arr[l] < arr[small]:
        small = l
        # arr[l] , arr[small] = arr[small] ,arr[l]
        # downheap(arr,n,l)
    if r < n and arr[r] < arr[small]:
        small = r
    if (small  != i):
        arr[small] , arr[i] = arr[i] ,arr[small]
        downheap(arr,n,small)
        
       

def buildHeap(arr,n):
    # code here

    for i in range(n):
        heapify(arr, n,i )
    # print(arr)  ∂    # res[0], res[len(res)] = res[len(res)], res[0]
    # return res          
         
 
def HeapSort(arr, n):
    res = []
    buildHeap(arr,len(arr))
    while(arr):
        res.append(arr.pop(0))
        heapify(arr,len(arr),0)
        print(res,arr)
        
    print(res)
       
    # res = []
    # arr2 = []
    # def const(res, n):
    #     for i in range(len(arr)):
    #         res.append(arr[i])
    #         buildHeap(res, len(res))
    #         print(res)
        
    
    # i = 0
    # while(i>n):
    #     arr2.append(res.pop(0))
    #     const(res, len(res))
    #     i += 1
    # print(arr2)


HeapSort(arr, len(arr))
# print(arr)
# buildHeap(arr,len(arr))

# vr =[4,3,2,1]
# upheap(vr,4,3)
# downheap(vr,4,0)
print(arr)



# if 2*i+1 < n:
            #     heapify(arr, n, 2*i+1)
            #     if arr[2*i+1]<arr[i]:
            #         arr[i], arr[2*i+1] = arr[2*i+1], arr[i]
            # if 2*i+2 < n:
            #     heapify(arr, n, 2*i+2)
            #     if arr[2*i+2]<arr[i]:
            #         arr[i], arr[2*i+2] = arr[2*i+2], arr[i]