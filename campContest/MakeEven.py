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
    s = insr()
    n = len(s)
    if not int(s[n-1])%2:
        print(0)
    elif not int(s[0])%2:
        print(1)
    else:
        found = False
        for j in range(1,n-1):
            if not int(s[j])%2:
                found = True
                break
        if found:
            print(2)
        else:
            print(-1)