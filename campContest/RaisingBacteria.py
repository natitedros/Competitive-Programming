import sys
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

num = inp()
nxt = 1
count = 1
while nxt != num:
    if nxt < num:
        nxt = nxt << 1
    elif nxt > num:
        num = num - (nxt>>1)
        nxt = 1
        count += 1
print(count)
