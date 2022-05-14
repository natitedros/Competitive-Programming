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
s = insr()
t = insr()
lens = len(s)
lent = len(t)
sptr = lens-1
tptr = lent-1
while sptr>=0 and tptr>=0 and s[sptr] == t[tptr]:
    sptr-=1
    tptr-=1
print(sptr+tptr+2)