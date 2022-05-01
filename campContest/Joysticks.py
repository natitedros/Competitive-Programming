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

j1, j2 = invr()
minutes = 0
while j1 > 0 and j2 > 0:
    if j2 < j1:
        j2 += 1
        j1 -= 2
    else:
        j1 += 1
        j2 -= 2
    minutes += 1
if j1<0 or j2 < 0:
    minutes -= 1
print(minutes) 