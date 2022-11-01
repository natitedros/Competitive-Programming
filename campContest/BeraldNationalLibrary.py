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
    total_cap = 0
    current_cap = 0
    inside = set()
    for _ in range(n):
        log, num = input().split()
        if log == "+":
            inside.add(num)
            current_cap += 1
        else:
            if num not in inside:
                total_cap += 1
            else:
                current_cap -= 1
                inside.remove(num)
            
        total_cap = max(current_cap, total_cap)
    print(total_cap)
        
main()