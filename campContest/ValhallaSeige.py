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
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
def main():
    n,q = invr()
    strength = inlt()
    arrows = inlt()
    prefix = [strength[0]]
    for i in range(1,n):
        prefix.append(strength[i]+prefix[i-1])
    search = 0
    for a in arrows:
        left,right = 0,n-1
        search += a
        while left <= right:
            mid = left+(right-left)//2
            if prefix[mid] > search:
                right = mid-1
            else:
                left = mid+1
        ans = n-left
        if ans == 0:
            print(n)
            search = 0
        else:
            print(ans)
main()
