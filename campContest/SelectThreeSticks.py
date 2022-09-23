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
    arr = inlt()
    arr.sort()
    minturn = math.inf
    for i in range(1,n-1):
        minturn = min(minturn,(arr[i]-arr[i-1])+(arr[i+1]-arr[i]))
    print(minturn)