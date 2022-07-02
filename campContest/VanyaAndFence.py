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
n, h = invr()
arr = inlt()
width = 0
for p in arr:
    if p > h:
        width += 2
    else:
        width += 1
print(width)