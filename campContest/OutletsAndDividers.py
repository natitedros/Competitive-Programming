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
for i in range(test):
    n, m = invr()
    dividers = inlt()
    dividers.sort()
    dividers.reverse()
    outlets = 2
    counter = 0
    for i in range(m):
        if outlets >= n:
            break
        counter += 1
        outlets += dividers[i]-1
    if outlets < n:
        print(-1)
    else:
        print(counter) 