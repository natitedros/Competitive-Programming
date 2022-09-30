import sys
from collections import defaultdict
import math
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
n = inp()
tiles = inlt()
d = {1:0,2:0}
for t in tiles:
    d[t] += 1
res = []
if d[2]:
    res.append(2)
    d[2] -= 1
    if d[1]:
        res.append(1)
        d[1] -= 1
while d[2]:
    res.append(2)
    d[2] -= 1
while d[1]:
    res.append(1)
    d[1] -= 1
print(*res)
        