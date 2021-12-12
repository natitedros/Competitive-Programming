def countingSort(arr):
    # Write your code here
    counter = [0]*len(arr)
    for i in range(len(arr)):
        counter[arr[i]]+=1
    return counter
