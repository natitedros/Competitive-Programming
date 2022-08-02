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
if bx<ax and by<ay:
    if cx<ax and cy<ay:
        print("YES")
    else:
        print("NO")
elif bx<ax and by>ay:
    if cx<ax and cy>ay:
        print("YES")
    else:
        print("NO")
elif bx>ax and by<ay:
    if cx>ax and cy<ay:
        print("YES")
    else:
        print("NO")
else:
    if cx>ax and cy>ay:
        print("YES")
    else:
        print("NO")