import sys
input = sys.stdin.readline
from collections import deque

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
arr = [1,5,10,20,100]
res = 0
for i in range(4,-1,-1):
    if n//arr[i] > 0:
        res += n//arr[i]
        n%=arr[i]
print(res)