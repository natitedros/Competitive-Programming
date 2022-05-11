from cmath import inf
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
    n = inp()
    candies = inlt()
    minVal = inf 
    for j in range(n):
        if candies[j] < minVal:
            minVal = candies[j]
    res = 0
    for j in range(n):
        res += candies[j]-minVal
    print(res)