def countingSort(arr):
    # Write your code here
    counter = [0]*(max(arr)+1)
    for i in range(len(arr)):
        counter[arr[i]]+=1
    return counter
