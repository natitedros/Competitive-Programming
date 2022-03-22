def insertionSort1(n, arr):
    # Write your code here
    carrier = arr[n-1]
    for i in range(n-1,0,-1):
        if carrier < arr[i-1]:
            arr[i]=arr[i-1]
            print(*arr)
        elif carrier >= arr[i-1]:
            arr[i] = carrier
            print(*arr)
            break
        if i==1 and arr[i-1]>carrier:
            arr[i-1] = carrier
            print(*arr)
