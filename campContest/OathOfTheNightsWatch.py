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
n = inp()
nums = inlt()
minVal = math.inf
maxVal = -math.inf
for num in nums:
    minVal = min(minVal,num)
    maxVal = max(maxVal,num)
res = 0
for num in nums:
    if minVal < num < maxVal:
        res += 1
print(res)
    