import sys
from collections import defaultdict
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)-1]))
    
def main():
    for _ in range(inp()):
        n = inp()
        grid = []
        grid.append(insr())
        grid.append(insr())
        dp = defaultdict(bool)
        dp[(1,n-1)] = (grid[1][n-1] == "0")
        if not dp[(1, n-1)]:
            print("NO")
        else:
            
            dp[(1,n-1)] = True
            for col in range(n-1, -1, -1):
                for row in range(1, -1, -1):
                    if row == 1 and col == n-1:
                        continue
                    dp[(row,col)] = (grid[row][col] == "0")
                    diag = dp[(row+1,col+1)]
                    antidiag = dp[(row-1,col+1)]
                    side = dp[(row,col+1)]
                    down = dp[(row+1, col)]
                    temp = diag or antidiag or side or down
                    dp[(row,col)] &= temp
            if dp[(0,0)]:
                print("YES")
            else:
                print("NO")
                
main()
    