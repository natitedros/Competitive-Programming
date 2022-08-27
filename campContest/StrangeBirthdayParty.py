import sys
input = sys.stdin.readline
from collections import defaultdict

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
    n, m = invr()
    friends = inlt()
    present = inlt()
    arr = sorted(friends,reverse=True)
    minVal = 0
    cost = 0
    for i in range(n):
        if minVal >= arr[i]-1:
            cost += present[arr[i]-1]
        else:
            cost += present[minVal]
            minVal += 1
    print(cost)