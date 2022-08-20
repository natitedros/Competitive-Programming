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
    left,right = 0,0
    found = False
    maxRes = [0,1]
    while right < n:
        s += arr[right]
        while left < n and s < 0:
            s -= arr[left]
            left += 1
        if maxRes[0]-maxRes[1]+1 < right-left+1:
            found =True
            maxRes = [right,left]
        right += 1
    if not found:
        print(-1)
    else:
        print(maxRes[1]+1,maxRes[0]+1)