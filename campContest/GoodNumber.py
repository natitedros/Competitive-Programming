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
n,k = invr()
vals = set()
for i in range(k+1):
    vals.add(i)
res = 0
for k in range(n):
    temp = set()
    num = insr()
    for char in num:
        temp.add(int(char))
    good = True
    for val in vals:
        if val not in temp:
            good = False
    if good:
        res += 1
print(res)
