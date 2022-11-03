import sys,heapq
from collections import defaultdict,deque
import math
sys.setrecursionlimit(100000)
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

def dfsBack(person, result, back, pos):
    p = person
    for i in range(pos, len(result), 2):
        result[i] = p
        p = back[p]
    
def main():
    n = inp()
    front = {}
    back = defaultdict(int)
    degree = defaultdict(int)
    
    start1 = 0
    start2 = 0
    for _ in range(n):
        f, b = invr()
        if f == 0:
            start2 = b
        back[f] = b
        degree[f] += 0
        degree[b] += 1
        
    for key in degree.keys():
        if degree[key] == 0:
            start1 = key
            break
        
    result = [0]*n
    
    dfsBack(start1, result, back, 0)
    
    dfsBack(start2, result, back, 1)
    
    print(*result)
    
    
main()