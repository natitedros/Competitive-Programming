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
n,d = invr()
friends = []
for k in range(n):
    m,f = invr()
    friends.append([m,f])
friends.sort()
maxF = 0
left = 0
F = 0
for right in range(n):
    F += friends[right][1]
    while friends[right][0]-friends[left][0] >= d:
        F -= friends[left][1]
        left += 1
    maxF = max(maxF,F)
print(maxF)
            
        