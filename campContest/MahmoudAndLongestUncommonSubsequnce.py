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
a = insr()
b = insr()
if a == b:
    print(-1)
else:
    lena=len(a)
    lenb=len(b)
    if lenb > lena:
        print(lenb)
    else:
        print(lena)