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
p = inlt()
q = inlt()
passed = set()
for i in range(1,p[0]+1):
    passed.add(p[i])
for i in range(1,q[0]+1):
    passed.add(q[i])
found = False
for i in range(1,n+1):
    if i not in passed:
        found = True
        break
if found:
    print("Oh, my keyboard!")
else:
    print("I become the guy.")