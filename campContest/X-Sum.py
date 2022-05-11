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
    maxD1 = max(d1, key=d1.get)
    maxD2 = max(d2, key=d2.get)
    row = maxD1-maxD2
    col = maxD1+maxD2
    print(d1[maxD1]+d2[maxD2]-grid[row][col])