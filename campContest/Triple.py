import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
tries = inp()
for i in range(tries):
    length = inp()
    arr = inlt()
    if length < 3:
        print(-1)
    else:
        d = {}
        for j in range(length):
            if arr[j] not in d:
                d[arr[j]] = 0
            d[arr[j]] += 1
            if d[arr[j]] >= 3:
                print(arr[j])
                break
            if j == length-1:
                print(-1)