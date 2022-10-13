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
love = [0]+inlt()
found = False
for i in range(1,n+1):
    if love[love[love[i]]] == i:
        found = True
if found:
    print("YES")
else:
    print("NO")
    