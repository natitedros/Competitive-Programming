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
s1 = insr()
s2 = insr()
lens1 = len(s1)
res = 0
for i in range(lens1):
    if ord(s1[i].upper()) > ord(s2[i].upper()):
        res = 1
        break
    elif ord(s1[i].upper()) < ord(s2[i].upper()):
        res = -1
        break
print(res)