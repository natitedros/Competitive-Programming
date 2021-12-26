arr = s*(math.ceil(n/len(s)))
    arr = ''.join(arr)
    counter = 0
    for i in range(0,n,1):
        if arr[i]=="a":
            counter += 1
    return counter