import sys
from collections import defaultdict
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
nums.sort()
left = 0
res = 0
for right in range(n):
    while left<right and nums[right]-nums[left]>5:
        left += 1
    res = max(res,right-left+1)
print(res)