
def countingSort(arr):
    # Write your code here
    counter = [0]*100
    for i in range(len(arr)):
        counter[arr[i]]+=1
    return counter

print(countingSort([0,0,1]))