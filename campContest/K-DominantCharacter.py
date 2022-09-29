import sys
from collections import defaultdict
import math
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
n=len(s)
d = defaultdict(list)
for i in range(n):
    d[s[i]].append(i)
minVal = math.inf
for key in d.keys():
    temp = d[key][0]+1
    for i in range(1,len(d[key])):
        temp=max(temp,d[key][i]-d[key][i-1])
    temp = max(temp,n-d[key][-1])
    minVal = min(minVal,temp)
print(minVal)
    
    