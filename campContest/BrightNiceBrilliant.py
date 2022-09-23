import sys
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
for k in range(test):
    n = inp()
    for i in range(1,n+1):
        row = []
        for j in range(1,i+1):
            if j == 1 or j == i:
                row.append(1)
            else:
                row.append(0)
        print(*row, sep=" ")
            