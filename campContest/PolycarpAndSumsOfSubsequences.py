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
    b = inlt()
    a1 = b[0]
    a2 = b[1]
    a3 = b[6]-(a1+a2)
    print(a1," ",a2," ",a3)