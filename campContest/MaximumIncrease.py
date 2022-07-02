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
n = inp()
arr = inlt()
if n == 1:
    print(1)
else:
    maxSub = 0
    temp = 1
    for i in range(1,n):
        if arr[i-1]<arr[i]:
            temp += 1
        else:
            maxSub = max(maxSub, temp)
            temp = 1
    maxSub = max(maxSub, temp)
    print(maxSub)