from collections import defaultdict
from email.policy import default
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
    n, m = invr()
    grid = []
    for i in range(n):
        grid.append(inlt())
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for i in range(n):
        for j in range(m):
            d1[i+j] += grid[i][j]
            d2[i-j] += grid[i][j]
    res = 0
    for i in range(n):
        for j in range(m):
            temp = d1[i+j] + d2[i-j] - grid[i][j]
            if temp > res:
                res = temp
    print(res)