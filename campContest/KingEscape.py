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
n = inp()
ax,ay = invr()
bx,by = invr()
cx,cy = invr()
chessDir = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
queenRange = set()
def queens(x,y,ind):
    if 0<=x<n and 0<=y<n:
        queenRange.add((x,y))
        r,c = chessDir[ind]
        x += r
        y += c
        return queens(x,y,ind)
    else:
        return 0
for i in range(8):
    queens(ax,ay,i)
dp = {}
def kings(x,y):
    if (x,y) in dp:
        return dp[(x,y)]
    if (x,y) in queenRange or x < 0 or y < 0 or x >= n or y >= n:
        return False
    elif (x,y) == (cx,cy):
        return True
    else:
        dp[(x,y)] = False
        for i in range(8):
            r,c = chessDir[i]
            new_r, new_c = x+r,y+c
            dp[(x,y)] |= kings(new_r,new_c)
            if dp[(x,y)]:
                return dp[(x,y)]
        return dp[(x,y)]
if kings(bx,by):
    print("YES")
else:
    print("NO")