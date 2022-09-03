import sys
input = sys.stdin.readline
from collections import defaultdict

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
s = insr()
balance = 0
d = {0:-1}
res = 0
for i in range(n):
    if s[i] == '1':
        balance += 1
    else:
        balance -= 1
    if balance not in d:
        d[balance] = i
    else:
        res = max(res,i-d[balance])
print(res)
