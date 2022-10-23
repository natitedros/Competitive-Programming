import sys,heapq
from collections import defaultdict,deque
import math
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)-1]))
def invr():
    return(map(int,input().split()))


def main():
    n = inp()
    row1 = inlt()
    row2 = inlt()
    dp = defaultdict(int)
    for i in range(n-1,-1,-1):
        dp[(i,True)] = max(row1[i]+dp[(i+1,False)], dp[(i+1,True)])
        dp[(i,False)] = max(row2[i]+dp[(i+1,True)], dp[(i+1, False)])
    maxLength = max(dp[(0,True)], dp[(0,False)])
    print(maxLength)
    
main()

