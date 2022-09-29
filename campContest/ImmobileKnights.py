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
    
test = inp()

direction = [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]
def isValid(row,col,n,m):
    temp = False
    for r,c in direction:
        temp |= (0<row+r<n+1) and (0<col+c<m+1)
    return temp
    
for k in range(test):
    n,m = invr()
    printed = False
    for i in range(1,n+1):
        for j in range(1,m+1):
            if not isValid(i,j,n,m) and not printed:
                print(i,j)
                printed = True
    if not printed:
        print(n,m)
        