import sys
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
    n,m = invr()
    grid = []
    for i in range(n):
        grid.append(insr())
    for i in range(n-2,-1,-1):
        for j in range(m):
            if grid[i][j] == "*":
                ptr = i
                while ptr < n-1 and grid[ptr+1][j] == ".":
                    ptr += 1
                grid[i][j] = "."
                grid[ptr][j] = "*"
    for row in grid:
        print(''.join(row))