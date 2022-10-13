import sys
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
n,m,k = inlt()
grid = []
for i in range(n):
    grid.append(insr())
if k:
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    def isValid(row,col):
        0<=row<n and 0<=col<m
    def validNeighbours(i,j):
        res = 0
        for r,c in dirs:
            newr = i+r
            newc = j+c
            if isValid(newr,newc) and grid[newr][newc] == ".":
                res += 1
        return res
    q = deque()
    neigh = defaultdict(int)
    minNeigh = math.inf
    mincell = (0,0)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                neigh[(i,j)] = validNeighbours(i,j)
                if neigh[(i,j)] < minNeigh:
                    minNeigh = neigh[(i,j)]
                    mincell = (i,j)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "." and neigh[(i,j)] == minNeigh:
                q.append((i,j))
    while q:
        row,col = q.popleft()
        grid[row][col] = "X"
        k -= 1
        if k:
            for r,c in dirs:
                newr = row+r
                newc = col+c
                if isValid(newr,newc) and grid[newr][newc] == ".":
                    neigh[(newr,newc)] -= 1
                    if neigh[(newr,newc)] == minNeigh:
                        q.append((newr,newc))
        else:
            q = None
for gr in grid:
    print(''.join(gr))
