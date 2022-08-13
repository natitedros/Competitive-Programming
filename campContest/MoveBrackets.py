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
    arr = insr()
    stk = []
    count = 0
    for i in range(n):
        if not stk and arr[i] == ")":
            count += 1
        elif arr[i] == ")":
            stk.pop()
        else:
            stk.append(arr[i])
    count += len(stk)
    print(count//2)
        