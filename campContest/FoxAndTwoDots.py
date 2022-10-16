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
    n,m = invr()
    grid = []
    
    for i in range(n):
        grid.append(insr())
        
    color = defaultdict(int)
    
    def isValid(row,col):
        return 0<=row<n and 0<=col<m
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    
    def dfs(i,j,prev):
        if color[(i,j)] == 1:
            return True
        if color[(i,j)] == 2:
            return False
        color[(i,j)] = 1
        for r,c in dirs:
            if isValid(i+r,j+c) and grid[i+r][j+c] == grid[i][j] and (i+r,j+c) != prev:
                if dfs(i+r,j+c,(i,j)):
                    return True
        color[(i,j)] = 2
        return False
    
    res = False
    for i in range(n):
        for j in range(m):
            if dfs(i,j,None):
                res = True
                break
    
    if res:
        print("Yes")
    else:
        print("No")
main()

