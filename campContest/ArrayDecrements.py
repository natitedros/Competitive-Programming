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
    n = inp()
    a = inlt()
    b = inlt()
    res = "YES"
    prev = 0
    for i in range(n):
        prev = max(prev,a[i]-b[i])
    for i in range(n):
        if (b[i] !=0 and a[i] - b[i] != prev) or (a[i] >= 0 and b[i] < 0):
            res = "NO"
            break
    print(res)