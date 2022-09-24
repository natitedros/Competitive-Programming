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
    T = insr()
    res = 0
    visited = set()
    for i in range(1,n+1):
        coeff = 1
        while coeff*i<=n:
            if T[(coeff*i)-1] == "0" and (coeff*i)-1 not in visited:
                res += i
                visited.add((coeff*i)-1)
                coeff += 1
            elif T[(coeff*i)-1] == "1":
                break
    print(res)