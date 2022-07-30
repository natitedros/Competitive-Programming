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
    n, s = invr()
    arr = inlt()
    left, right, maxLen = 0,0,0
    sm = 0
    found = False
    while right < n:
        sm += arr[right]
        while sm > s:
            sm -= arr[left]
            left += 1
        if sm == s:
            found = True
            maxLen = max(maxLen,right-left+1)
        right += 1
    if found:
        print(n-maxLen)
    else:
        print(-1)