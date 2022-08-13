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

test = inp()
for k in range(test):
    n,k = invr()
    arr = inlt()
    temp = [0]*31
    for num in arr:
        length = num.bit_length()
        for j in range(length):
            if num&(1<<j):
                temp[j] += 1
    for i in range(30,-1,-1):
        if n-temp[i] <= k:
            k -= (n-temp[i])
            temp[i] = n
    res = 0
    for i in range(30,-1,-1):
        res = res<<1
        if temp[i] == n:
            res |= 1
    print(res)