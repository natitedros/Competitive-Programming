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
    test = inp()
    for _ in range(test):
        n = inp()
        stacks = inlt()
        for i in range(n-1):
            if stacks[i] >= i:
                stacks[i+1] += stacks[i]-i
                stacks[i] = i
        isIncreasing = True
        for i in range(1,n):
            if stacks[i] <= stacks[i-1]:
                isIncreasing = False
                break
        if isIncreasing:
            print("YES")
        else:
            print("NO")
            
main()

